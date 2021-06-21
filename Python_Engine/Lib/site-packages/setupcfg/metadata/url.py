#!/usr/bin/env python
"""read/write `setup.cfg` `[metadata]` `url`"""
import click
import setupcfg

SECTION = "metadata"
KEY = "url"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [url]' % MODULE_NAME


@click.command()
@click.argument(KEY, required=False)
def _cli(url=None):
    cfg = setupcfg.load()
    if url is not None:
        cfg[SECTION][KEY] = url
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print(cfg[SECTION][KEY])


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
