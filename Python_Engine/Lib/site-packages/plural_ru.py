#!/usr/bin/env python
"""выводит строку со склоненным существительным"""
# -*- coding: utf-8 -*-
import click
import os
import public


@public.add
def ru(value, quantitative):
    """возвращает строку со склоненным существительным"""
    if value % 100 in (11, 12, 13, 14):
        return quantitative[2]
    if value % 10 == 1:
        return quantitative[0]
    if value % 10 in (2, 3, 4):
        return quantitative[1]
    return quantitative[2]


MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s count quantitative1 quantitative2 quantitative3' % MODULE_NAME


@click.command()
@click.argument('count', required=True)
@click.argument('quantitative1', required=True)
@click.argument('quantitative2', required=True)
@click.argument('quantitative3', required=True)
def _cli(count, quantitative1, quantitative2, quantitative3):
    quantitative = [quantitative1, quantitative2, quantitative3]
    print(ru(int(count), quantitative))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
