Evasion Common
==============

.. contents::

EvasionProject code documentation
---------------------------------

  * http://www.evasionproject.com/apidocs/


EvasionProject Wiki
-------------------

  * http://www.evasionproject.com/


Introduction
------------

This package provides "evasion.common". This is a collection of useful functions
and other utilities.


evasion.common.net
------------------

get_free_port
~~~~~~~~~~~~~

Find a TCP port locally that is not in use and return it. This finds a random
port in the range 2000 - 10000. It tests if it is available by binding to it. It
the closed the socket and return the port.

This is quite handy for getting a free port to run a service on while acceptance
testing.

Example usage::

    from evasion.common import net

    # Get a free port:
    port1 = net.get_free_port()

    # Get another free port excluding the first port from the list
    port1 = net.get_free_port(exclude_ports=[port1])


wait_for_ready
~~~~~~~~~~~~~~

Called to wait for a web application to respond to normal requests. This is
useful when you want to know a web app is not just bound to a socket, but is
actually responding 200 OK to root page downloads.

Example usage from unit tests::

    from evasion.common import net
    from evasion.common import webhelpers

    port1 = net.get_free_port()

    # Run the web app and wait for ready should connect:
    web = webhelpers.BasicWeb(port=port1)
    web.start()

    result = net.wait_for_ready(web.uri)
    assert result

    web.stop()


wait_for_service
~~~~~~~~~~~~~~~~

Called to wait until a socket connection can be made to a remote service.


Example usage from unit tests::

    from evasion.common import net
    from evasion.common import webhelpers

    port1 = net.get_free_port()

    # Run the web app and wait for ready should connect:
    web = webhelpers.BasicWeb(port=port1)
    web.start()

    result = net.wait_for_service('localhost', port1)
    assert result

    web.stop()


