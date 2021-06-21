#!/usr/bin/env python
from collections import OrderedDict
import public

"""
http://setuptools.readthedocs.io/en/latest/setuptools.html#specifying-values
TypeError: option values must be strings
convert config items to string values

str - simple string
list-comma - dangling list or string of comma-separated values
list-semi - dangling list or string of semicolon-separated values
bool - True is 1, yes, true
dict - list-comma where keys are separated from values by =
"""


def _bool2string(value):
    return "1" if value else "0"


def _list2string(value):
    if value:
        return "\n%s" % "\n".join(sorted(filter(None, value)))


def _dict2list(value):
    for k, v in value.items():
        yield "%s = %s" % (k, v)


def _dict2string(value):
    return _list2string(list(_dict2list(value)))


def _string2list(string):
    return string.splitlines()[1:]


def _string2dict(string):
    lines = _string2list(string)
    result = dict()
    for line in lines:
        key, value = line.split(" = ")
        result[key] = value
    return result


@public.add
def string(value):
    """Convert a value to a `setup.cfg` value string"""
    if isinstance(value, bool):
        return _bool2string(value)
    if isinstance(value, (list, set, tuple)):
        return _list2string(value)
    if isinstance(value, dict):
        return _dict2string(value)
    return str(value).rstrip()


@public.add
def value(string):
    """Convert a string to a python value"""
    if len(string.splitlines()) > 1 and not string.splitlines()[0]:
        if " = " in string:
            return _string2dict(string)
        return _string2list(string)
    if string.strip() in ["0", "1"]:
        return bool(int(string.strip()))
    return string.lstrip().rstrip()
