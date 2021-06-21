#!/usr/bin/env python
"""read/write `setup.cfg` `[options]` `install_requires`"""
import click
import setupcfg

SECTION = "options"
KEY = "install_requires"


MODULE_NAME = "setupcfg.%s.%s" % (SECTION, KEY)
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [requires ...]' % MODULE_NAME


@click.command()
@click.argument(KEY, nargs=-1, required=False)
def _cli(install_requires=None):
    cfg = setupcfg.load()
    if install_requires:
        cfg[SECTION][KEY] = install_requires
        if not install_requires[0]:
            del cfg[SECTION][KEY]
        cfg.save()
    else:
        if KEY in cfg[SECTION]:
            print("\n".join(cfg[SECTION][KEY]))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
