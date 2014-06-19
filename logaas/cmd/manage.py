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

"""CLI for LogaaS management."""

from __future__ import print_function

import sys

from logaas.cmd import cliutils
from logaas import db


class DBCommands(object):
    """Commands for DB management."""

    def create(self):
        """Create database for logaas."""
        db.db_create()

    def recreate(self):
        """Drop and then create database for logaas."""
        db.db_drop()
        db.db_create()


def main():
    categories = {'db': DBCommands}
    cliutils.run(sys.argv, categories)


if __name__ == '__main__':
    main()
