#!/usr/bin/env python
"""close url(s)"""
import click
import google_chrome

MODULE_NAME = "google_chrome.close"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [url ...]' % MODULE_NAME


@click.command()
@click.argument("url", nargs=-1, required=False)
def _cli(url=None):
    google_chrome.close(url)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
