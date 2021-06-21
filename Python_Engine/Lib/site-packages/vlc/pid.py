#!/usr/bin/env python
"""print VLC.app pid"""
import vlc

if __name__ == "__main__":
    pid = vlc.pid()
    if pid:
        print(pid)
