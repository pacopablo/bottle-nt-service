bottle-nt-service
=================

Code for running a bottle.py app as a Windows NT Service


Service Insanity
=======================

It may come as a shock to some, but strangely enough, Windows <> \*nix.
Daemonizing services works great on \*nix.  Not so much on Windows.  The
proper way to run a server is as a service.  So, if you can't do something
smart, do something right.  Unfortunately, Windows NT Services are not a
natural fit for Python web frameworks.  Because of this, getting a `bottle.py`
app to run as a Windows NT Service requires more manual processes than
desired. Additionally, running as a service currently requires the use of the
`WSGIRefServer`, which isn't as performant as some of the others.


Putting it together
====================

The `bottle_service.py` file contains the main code for installing and running
as a service.  This requires some changes to be made for each `bottle.py` app
one wants to run as a service.

Things to change
-----------------

* Rename the  `bottle_service.py`  to differentiate it if installing multiple
  services.  The basename of the file will be used as the service short name.

* Change the `__display_name__` and  `__description__` values in
  `bottle_service.py`.  These correspond to the service display name and
  description.

* Locate the section `# Import your app here` and change the import
  accordingly.

* Set the `__host__` and `__port__` to desired values.  Default is to bind to
  `0.0.0.0:8042`



Caveats
========

#. Virtualenvs are right out.  I can't think of a way to use Windows NT Services
   in conjunction with virutal envs.

#. The service only needs to be installed once.  One can replace the
   script/module containing the app and it will be reloaded the next time the
   service is restarted.


Installation
=============

Open up a command prompt as adminitrator (right->click, "Run as
Administrator" ) and type::

  python bottle_service.py install


Desires
========

I want to remove a much manual fiddling as possible.  A few ideas are:

* Use the registry to store the `__host__` and `__port__` info.

  * Create default handler to allow setting of `___host__` and `__port__` if
    not set

* Take service name, description, etc. via the command line.  Will need to
  deal with handling of service functions such as `install` as well.

* Work with `py2exe` or somesuch to be able to package services better


