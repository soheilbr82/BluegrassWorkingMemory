#!/usr/bin/env python
import decorator
import public
import detect


def _raise_if(value, f, msg):
    if value:
        name = "%s.%s" % (f.__module__, f.__name__)
        raise OSError("%s %s" % (name, msg))


@decorator.decorator
def linux(f, *args, **kwargs):
    """`@only.linux` decorator. raise OSError in not linux"""
    _raise_if(not detect.linux, f, "is Linux only :(")
    return f(*args, **kwargs)


@decorator.decorator
def mac(f, *args, **kwargs):
    """`@only.mac` decorator. raise OSError in not MacOS"""
    _raise_if(not detect.mac, f, "is MacOS only :(")
    return f(*args, **kwargs)


@decorator.decorator
def osx(f, *args, **kwargs):
    """`@only.osx` decorator. raise OSError in not OSX"""
    _raise_if(not detect.mac, f, "is OSX only :(")
    return f(*args, **kwargs)


@decorator.decorator
def windows(f, *args, **kwargs):
    """`@only.windows` decorator. raise OSError in not Windows"""
    _raise_if(not detect.mac, f, "is OSX only :(")
    return f(*args, **kwargs)


@decorator.decorator
def unix(f, *args, **kwargs):
    """`@only.unix` decorator. raise OSError in not Unix"""
    _raise_if(not detect.unix, f, "is OSX only :(")
    return f(*args, **kwargs)


public.add(linux, mac, osx, unix, windows)
