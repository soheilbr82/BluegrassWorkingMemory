#!/usr/bin/env python
import setupcfg.metadata
import setupcfg.options
import setupcfg.values
from setupcfg.cfg import Setupcfg
import public

public.add(Setupcfg)


@public.add
def get(section, option, default=None):
    """return the value for option if option is in the `setup.cfg`, else default"""
    cfg = Setupcfg().load("setup.cfg")
    return cfg.get(section, {}).get(option, default)


@public.add
def load(path="setup.cfg"):
    """return dictionary with `setup.cfg` sections dictionaries"""
    return Setupcfg().load(path)
