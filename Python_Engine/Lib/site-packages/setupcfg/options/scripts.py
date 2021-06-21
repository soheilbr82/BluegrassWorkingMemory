#!/usr/bin/env python
"""read/write `setup.cfg` `[options]` `scripts`"""
import click
import setupcfg

SECTION = "options"
KEY = "scripts"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [script ...]' % MODULE_NAME


@click.command()
@click.argument(KEY, nargs=-1, required=False)
def _cli(scripts=None):
    cfg = setupcfg.load()
    if scripts:
        cfg[SECTION][KEY] = scripts
        if not scripts[0]:
            del cfg[SECTION][KEY]
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print("\n".join(cfg[SECTION][KEY]))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
