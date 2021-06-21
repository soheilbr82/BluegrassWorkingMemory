#!/usr/bin/env python
import public


def _reverse(string):
    chars = list(string)
    chars.reverse()
    return "".join(chars)


@public.add
def rreplace(string, old, new, count=None):
    """string right replace"""
    string = str(string)
    r = _reverse(string)
    if count is None:
        count = -1
    r = r.replace(_reverse(old), _reverse(new), count)
    return type(string)(_reverse(r))
