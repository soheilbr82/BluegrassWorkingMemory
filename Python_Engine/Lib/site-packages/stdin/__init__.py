#!/usr/bin/env python
import os
import sys

__all__ = ["STDIN"]


def _read_stdin():
    if os.fstat(sys.stdin.fileno()).st_size > 0:
        return sys.stdin.read()


STDIN = _read_stdin()
