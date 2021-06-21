#!/usr/bin/env python
"""start iLifeSlideshows screensaver"""
import click
import mac_slideshow

MODULE_NAME = "mac_slideshow.start"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [path]' % MODULE_NAME


@click.command()
@click.argument('path', required=False)
def _cli(path):
    mac_slideshow.start(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
