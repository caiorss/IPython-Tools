#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ipython Extension for Persistent directory bookmark.

"""

import shelve
import os
from pprint import pprint


from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class BookMarkMagics(Magics):
    """A simple Hello, <name> magic.

    """

    @line_magic  # or ``@line_magic("hi")`` to make ``%hi`` the name of the magic
    def markdir(self, line='', cell=None):
        """

        Example::

            %markdir   <path>  <bookrmark-name>

            %markdir   /home/tux/PycharmProject/project1  proj1

            %markdir  this  Bookmark1

        this: Gets the current directory

        """
        bookmarksdb = os.path.join(os.path.expanduser("~"), ".markdir.db")
        args = line.split()

        if len(args) !=2:
            print("Usage: %markir <Path> <Name/Alias>")
            return

        path, name = args

        if path == "this":
            path = os.getcwd()

        db = shelve.open(bookmarksdb)
        db[name] = path
        db.close()


    @line_magic  # or ``@line_magic("hi")`` to make ``%hi`` the name of the magic
    def listdirs(self, line='', cell=None):
        """

        Example::

            %markdir   <path>  <bookrmark-name>

            %markdir   /home/tux/PycharmProject/project1  proj1

        """
        bookmarksdb = os.path.join(os.path.expanduser("~"), ".markdir.db")

        db = shelve.open(bookmarksdb)
        pprint(list(db.keys()))
        db.close()


    @line_magic  # or ``@line_magic("hi")`` to make ``%hi`` the name of the magic
    def go(self, line=''):
        """

        Example::

            %markdir   <path>  <bookrmark-name>

            %markdir   /home/tux/PycharmProject/project1  proj1

        """
        bookmarksdb = os.path.join(os.path.expanduser("~"), ".markdir.db")

        if line == "":
            print("Usage: %go <directory alias/>")
            return

        db = shelve.open(bookmarksdb)

        path = db[line]
        os.chdir(path)
        print("Changed to : %s" % path)


    @line_magic  # or ``@line_magic("hi")`` to make ``%hi`` the name of the magic
    def rmmark(self, line=''):
        """

        Example::

            %markdir   <path>  <bookrmark-name>

            %markdir   /home/tux/PycharmProject/project1  proj1

        """
        bookmarksdb = os.path.join(os.path.expanduser("~"), ".markdir.db")

        if line == "":
            print("Usage: %go <directory alias/>")
            return

        db = shelve.open(bookmarksdb)
        db.pop(line)
        db.close()

    @line_magic
    def opendir(self, line=''):
        from subprocess import Popen
        bookmarksdb = os.path.join(os.path.expanduser("~"), ".markdir.db")

        if line == "":
            path = os.getcwd()

        elif line.startswith("$"):

            name = line.split("$")[1].strip()
            db = shelve.open(bookmarksdb)
            path = db[name]
            db.close()

        else:
            path = line

        Popen(["xdg-open", path])

def load_ipython_extension(ip):
    ip.register_magics(BookMarkMagics)