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

import mock

from logaas.cmd import manage
from tests import test


class DBCommandsTestCase(test.TestCase):

    @mock.patch("logaas.cmd.manage.db")
    def test_create(self, mock_db):
        manage.DBCommands().create()
        mock_db.db_create.assert_called_once_with()

    @mock.patch("logaas.cmd.manage.db")
    def test_recreate(self, mock_db):
        manage.DBCommands().recreate()
        mock_db.db_drop.assert_called_once_with()
        mock_db.db_create.assert_called_once_with()
