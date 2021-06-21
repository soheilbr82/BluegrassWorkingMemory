#!/usr/bin/env python
import os
import public
import values


@public.add
def mkdir(path):
    """mkdir (if not exists)"""
    for path in values.get(path):
        fullpath = os.path.expanduser(path)
        if fullpath and not os.path.exists(fullpath):
            os.makedirs(fullpath)
