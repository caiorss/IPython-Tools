#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class HelloWorldMagics(Magics):
    """A simple Hello, <name> magic.

    """

    @line_magic  # or ``@line_magic("hi")`` to make ``%hi`` the name of the magic
    @cell_magic
    def helloworld(self, line='', cell=None):
        """Virtually empty magic for demonstration purposes.

        Example::

          In [1]: %load_ext helloworld

          In [2]: %helloworld Catherine
          Out[2]: u'Hello, Catherine'


        """
        return "Hello, %s\n%s" % (line, cell or "")

def load_ipython_extension(ip):
    ip.register_magics(HelloWorldMagics)