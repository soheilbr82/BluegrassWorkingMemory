#!/usr/bin/env python
"""print/set VLC volume (0..512)"""
import click
import public
import vlc


@public.add
def get():
    """return VLC volume"""
    if vlc.pid():
        return int(vlc.tell('audio volume'))


@public.add
def change(value):
    """set VLC volume"""
    vlc.tell('set audio volume to %s' % value)


MODULE_NAME = "vlc.volume"
USAGE = "python -m %s [volume]" % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
@click.argument('volume')
def _cli(volume=None):
    if volume:
        return change(int(volume))
    volume = get()
    if volume:
        print(volume)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
