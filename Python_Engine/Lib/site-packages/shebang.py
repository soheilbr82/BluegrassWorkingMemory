#!/usr/bin/env python
"""print script shebang"""
# -*- coding: utf-8 -*-s
import click
import os
import public


@public.add
def get(path):
    """return script shebang"""
    if os.path.exists(path):
        try:
            lines = open(path).read().splitlines()
            if lines and lines[0].find("#!") == 0:
                return lines[0].replace("#!", "").strip()
        except UnicodeDecodeError:
            pass


@public.add
def shebang(path):
    """return script shebang. deprecated"""
    return get(path)


MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
USAGE = 'python -m %s path' % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
@click.argument('path', required=True)
def _cli(path):
    value = shebang(path)
    if value:
        print(value)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
