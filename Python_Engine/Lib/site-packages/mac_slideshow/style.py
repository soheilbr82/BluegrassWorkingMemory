#!/usr/bin/env python
"""read/write iLifeSlideShows screensaver style"""
import click
import public
import mac_slideshow

"""
Classic
"""

KEY = "styleKey"


@public.add
def read():
    """return iLifeSlideShows style"""
    return mac_slideshow.preferences.read(KEY)


@public.add
def write(style):
    """write iLifeSlideShows style"""
    return mac_slideshow.preferences.write(KEY, style)


MODULE_NAME = "mac_slideshow.style"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [style]' % MODULE_NAME


@click.command()
@click.argument('style', required=False)
def _cli(style):
    if style:
        print(read())
    else:
        write(style)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
