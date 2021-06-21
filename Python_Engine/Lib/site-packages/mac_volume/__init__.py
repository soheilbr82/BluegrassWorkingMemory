#!/usr/bin/env python
# -*- coding: utf-8 -*-
import applescript
import public


def _execute(code):
    return applescript.run(code).out


@public.add
def get():
    """return volume"""
    out = _execute("output volume of (get volume settings)")
    return int(out)


@public.add
def change(volume):
    """change volume"""
    _execute("set volume output volume %s" % volume)


@public.add
def mute():
    """mute"""
    _execute("set volume with output muted")


@public.add
def muted():
    """return True if muted"""
    return "true" in _execute("output muted of (get volume settings)")


@public.add
def unmute():
    """unmute"""
    _execute("set volume without output muted")
