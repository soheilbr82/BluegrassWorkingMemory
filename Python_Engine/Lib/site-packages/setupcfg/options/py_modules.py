#!/usr/bin/env python
"""read/write `setup.cfg` `[options]` `py_modules`"""
import click
import setupcfg

SECTION = "options"
KEY = "py_modules"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [module ...]' % MODULE_NAME


@click.command()
@click.argument(KEY, nargs=-1, required=False)
def _cli(py_modules=None):
    cfg = setupcfg.load()
    if py_modules:
        cfg[SECTION][KEY] = py_modules
        if not py_modules[0]:
            del cfg[SECTION][KEY]
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print("\n".join(cfg[SECTION][KEY]))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
