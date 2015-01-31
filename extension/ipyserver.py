#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic


class Listener():
    def __init__(self, host='', port=8888):

        import socket
        import sys

        self.namespace = None

        self.host = host  # Symbolic name, meaning all available interfaces
        self.port = port  # Arbitrary non-privileged port

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.settimeout(1)
        #print 'Socket created'

        #Bind socket to local host and port
        self.sock = s


    def _main(self):

        # logger.warn("Starting socket server")

        import socket

        s = self.sock

        try:
            s.bind((self.host, self.port))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            pass


        # Start listening on socket
        s.listen(10)

        while 1:
            conn, addr = self.sock.accept()
            code = conn.recv(8049)
            conn.close()

            code = '\n' + code.decode("utf-8")
            print(code)

            try:
                bytecode = compile(code, '<string>', 'exec')
                exec(bytecode, globals())
            except Exception as err:
                print(err)
                print(err.args)
                print(err.__class__)

    def main(self):

        import threading

        server_thread = threading.Thread(target=self._main, args=())
        server_thread.daemon = True
        server_thread.start()


pyserver = Listener()



@magics_class
class IPythonServer(Magics):
    """A simple Hello, <name> magic.

    """

    @line_magic  # or ``@line_magic("hi")`` to make ``%hi`` the name of the magic
    @cell_magic
    def ipyserver(self, line='', cell=None):
        """Virtually empty magic for demonstration purposes.

        Example::

          In [1]: %load_ext helloworld

          In [2]: %helloworld Catherine
          Out[2]: u'Hello, Catherine'


        """
        print("Running server on Port : ", pyserver.port)
        pyserver.main()


def load_ipython_extension(ip):
    ip.register_magics(IPythonServer)