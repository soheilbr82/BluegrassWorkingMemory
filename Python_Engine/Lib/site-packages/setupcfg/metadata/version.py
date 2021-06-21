#!/usr/bin/env python
"""read/write `setup.cfg` `[metadata]` `version`"""
import click
import setupcfg

SECTION = "metadata"
KEY = "version"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [version]' % MODULE_NAME


@click.command()
@click.argument(KEY, required=False)
def _cli(version=None):
    cfg = setupcfg.load()
    if version is not None:
        cfg[SECTION][KEY] = version
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print(cfg[SECTION][KEY])


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
