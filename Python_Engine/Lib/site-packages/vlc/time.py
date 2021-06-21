#!/usr/bin/env python
"""print/set current video time"""
import click
import public
import vlc


@public.add
def get():
    """return current video time"""
    if vlc.pid():
        return int(vlc.tell('get current time'))


@public.add
def change(seconds):
    """set current video time"""
    vlc.tell('set current time to %s' % seconds)


MODULE_NAME = "vlc.time"
USAGE = "python -m %s [seconds]" % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
@click.argument('time')
def _cli(time=None):
    if time:
        return change(int(time))
    time = get()
    if time:
        print(time)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
