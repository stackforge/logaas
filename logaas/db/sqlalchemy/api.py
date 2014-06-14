# Copyright 2014: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
SQLAlchemy implementation for DB.API
"""

from oslo.config import cfg

from logaas.db.sqlalchemy import models
from logaas.openstack.common.db.sqlalchemy import session as db_session
from logaas.openstack.common.gettextutils import _


CONF = cfg.CONF

CONF.import_opt('connection',
                'logaas.openstack.common.db.options',
                group='database')

_FACADE = None


def _create_facade_lazily():
    global _FACADE

    if _FACADE is None:
        _FACADE = db_session.EngineFacade.from_config(
            CONF.database.connection, CONF)

    return _FACADE


def get_engine():
    facade = _create_facade_lazily()
    return facade.get_engine()


def get_session(**kwargs):
    facade = _create_facade_lazily()
    return facade.get_session(**kwargs)


def get_backend():
    """The backend is this module itself."""
    return Connection()


class Connection(object):

    def db_cleanup(self):
        global _FACADE

        _FACADE = None

    def db_create(self):
        models.create_db()

    def db_drop(self):
        models.drop_db()

    def model_query(self, model, session=None):
        """The helper method to create query.

        :param model: The instance of
                      :class:`logaas.db.sqlalchemy.models.LogaasBase` to
                      request it.
        :param session: Reuse the session object or get new one if it is
                        None.
        :returns: The query object.
        :raises: :class:`Exception` when the model is not a subclass of
                 :class:`logaas.db.sqlalchemy.models.RallyBase`.
        """
        session = session or get_session()
        query = session.query(model)

        def issubclassof_logaas_base(obj):
            return isinstance(obj, type) and issubclass(obj, models.LogaasBase)

        if not issubclassof_logaas_base(model):
            raise Exception(_("The model should be a subclass of LogaasBase"))

        return query
