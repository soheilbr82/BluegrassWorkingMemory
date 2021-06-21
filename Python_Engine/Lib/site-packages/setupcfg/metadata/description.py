#!/usr/bin/env python
"""read/write `setup.cfg` `[metadata]` `description`"""
import click
import setupcfg

SECTION = "metadata"
KEY = "description"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [description]' % MODULE_NAME


@click.command()
@click.argument(KEY, required=False)
def _cli(description=None):
    cfg = setupcfg.load()
    if description is not None:
        cfg[SECTION][KEY] = description
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print(cfg[SECTION][KEY])


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
