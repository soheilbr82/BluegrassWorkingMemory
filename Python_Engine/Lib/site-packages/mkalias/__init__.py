#!/usr/bin/env python
import os
import public
import runcmd


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


@public.add
def mkalias(src, dst):
    """make MacOS Finder alias"""
    cmd = ["mkalias", _fullpath(src), _fullpath(dst)]
    runcmd.run(cmd)._raise()
    """refresh icon"""
    os.utime(os.path.dirname(_fullpath(dst)), None)
