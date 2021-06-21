#!/usr/bin/env python
"""read/write `setup.cfg` `[metadata]` `name`"""
import click
import setupcfg

SECTION = "metadata"
KEY = "name"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [name]' % MODULE_NAME


@click.command()
@click.argument(KEY, required=False)
def _cli(name=None):
    cfg = setupcfg.load()
    if name is not None:
        cfg[SECTION][KEY] = name
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print(cfg[SECTION][KEY])


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
