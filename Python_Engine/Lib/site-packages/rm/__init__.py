#!/usr/bin/env python
import os
import shutil
import public
import values

"""
os.remove() removes a file.
os.rmdir() removes an empty directory.
shutil.rmtree() deletes a directory and all its contents.
pathlib.Path.unlink() removes the file or symbolic link.
pathlib.Path.rmdir() removes the empty directory.
"""


@public.add
def rm(path):
    """remove path(s) (if exists)"""
    for path in values.get(path):
        fullpath = os.path.abspath(os.path.expanduser(path))
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        if os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
