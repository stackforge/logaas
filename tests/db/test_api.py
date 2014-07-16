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


from logaas import db
from logaas.openstack.common.db import options as db_options
from tests import test


db_options.set_defaults(sql_connection='sqlite://', sqlite_db='logaas.sqlite')


class ManageDBTestCase(test.TestCase):

    def test_cleanup(self):
        # TODO(boris-42): Test more detailed when we will have something in db.
        db.db_cleanup()

    def test_create(self):
        # TODO(boris-42): Test more detailed when we will have something in db.
        db.db_create()

    def test_create_delete_create(self):
        # TODO(boris-42): Test more detailed when we will have something in db.
        db.db_create()
        db.db_drop()
        db.db_create()
