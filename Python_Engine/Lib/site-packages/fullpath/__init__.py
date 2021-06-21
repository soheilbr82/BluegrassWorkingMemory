#!/usr/bin/env python
import os
import public


@public.add
def fullpath(path):
    """return fullpath"""
    if path is None:
        return None
    return os.path.abspath(os.path.expanduser(path))
