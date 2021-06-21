#!/usr/bin/env python
import os
import public
import values


def _mkdir(path):
    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)


def _utime(path):
    try:
        os.utime(path, None)
    except Exception:
        open(path, 'a').close()


@public.add
def mktouch(path):
    """mkdir + touch"""
    for path in values.get(path):
        _mkdir(path)
        if not os.path.exists(path):
            open(path, "w").write("")
        else:
            _utime(path)
