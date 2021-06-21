#!/usr/bin/env python
"""read/write iLifeSlideShows screensaver path"""
import click
import public
import mac_slideshow


KEY = "SelectedFolderPath"


@public.add
def read():
    """return iLifeSlideShows images folder path"""
    return mac_slideshow.preferences.read(KEY)


@public.add
def write(path):
    """write iLifeSlideShows images folder path"""
    return mac_slideshow.preferences.write(KEY, path)


MODULE_NAME = "mac_slideshow.path"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [path]' % MODULE_NAME


@click.command()
@click.argument('path', required=False)
def _cli(path):
    if path:
        print(read())
    else:
        write(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
