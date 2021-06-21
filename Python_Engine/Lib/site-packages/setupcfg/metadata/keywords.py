#!/usr/bin/env python
"""read/write `setup.cfg` `[metadata]` `keywords`"""
import click
import setupcfg

SECTION = "metadata"
KEY = "keywords"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [keywords]' % MODULE_NAME


@click.command()
@click.argument(KEY, required=False)
def _cli(keywords=None):
    cfg = setupcfg.load()
    if keywords is not None:
        cfg[SECTION][KEY] = keywords
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print(cfg[SECTION][KEY])


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
