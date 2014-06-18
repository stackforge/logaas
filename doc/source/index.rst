..
      Copyright 2014 Mirantis Inc. All Rights Reserved.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

Logging as a Service for OpenStack documentation
================================================

**Don't worry we are not going to reinvent logstash & syslog.**

Why one more service?
---------------------

As you probably know OpenStack is quite large ecosystem of
multiply services that are collaborating together to implement
OpenStack API. Sometimes to implement one OpenStack API method
you need to use multiply OpenStack services. It goes without
saying words that it will be hard to debug such well distributed
system, especially if you don't have logs.

As we already known it's quite important to be able to store and
query log in OpenStack. But current OpenStack infrastructure won't
help you with this.

Missing standard way to deal with logs produce to big issues:
1) Everybody that would like to work with OpenStack have to build
custom logging system (duplicating of efforts)
2) We are not able to provide OpenStack API for working with logs,
as a result we are not able to retrieve LOGs from Horizon.
3) We are not able to collaborate together to build a system of
aggregation & smart analyze of logs.



Current goals
-------------

#. Allows to setup :on presented resources logging service (e.g. logstash)
#. Auto-scale of logging service
#. Querying logging service to retrieve logs
#. Integration with keystone that will allow project to auto discover where to
   store logs. No more billions changes in all `*.conf` files to setup logging
   in all services


Source Documentation
====================

Contents:

.. toctree::
   :maxdepth: 3



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
