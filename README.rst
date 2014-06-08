OpenStack Logging as a Service
==============================

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
3) We are not able to collabarate together to build a system of
aggregation & smart analyze of logs. 



Current goals
-------------

#. Allows to setup :on presented resources logging service (e.g. logstash)
#. Autoscale of logging service
#. Querying logging serivce to retrive logs
#. Integration with keystone that will allow project to auto discover where to
   store logs. No more billions changes in all `*.conf` files to setup logging
   in all services
