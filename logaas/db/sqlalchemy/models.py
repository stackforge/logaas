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
SQLAlchemy models for logaas data.
"""
import uuid

from sqlalchemy.ext.declarative import declarative_base

from logaas.openstack.common.db.sqlalchemy import models


BASE = declarative_base()


def UUID():
    return str(uuid.uuid4())


class LogaasBase(models.TimestampMixin,
                 models.ModelBase):
    metadata = None

    def save(self, session=None):
        from logaas.db.sqlalchemy import api as sa_api

        if session is None:
            session = sa_api.get_session()

        super(LogaasBase, self).save(session=session)


def create_db():
    from logaas.db.sqlalchemy import api as sa_api

    BASE.metadata.create_all(sa_api.get_engine())


def drop_db():
    from logaas.db.sqlalchemy import api as sa_api

    engine = sa_api.get_engine()
    OLD_BASE = declarative_base()
    OLD_BASE.metadata.reflect(bind=engine)
    OLD_BASE.metadata.drop_all(engine, checkfirst=True)
