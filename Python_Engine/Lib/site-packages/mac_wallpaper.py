#!/usr/bin/env python
"""get/set wallpaper path"""
import applescript
import click
import os
import public


@public.add
def get():
    """return wallpaper path"""
    return applescript.tell.app("System Events", "tell every desktop to picture").out


@public.add
def update(path):
    """update wallpaper path"""
    applescript.tell.app("System Events", """tell every desktop
    set picture to ("%s" as POSIX FILE)
end tell""" % path)


MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [path]' % MODULE_NAME


@click.command()
@click.argument('path', required=False)
def _cli(path=None):
    if path:
        update(path)
    else:
        print(get())


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
