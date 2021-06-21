#!/usr/bin/env python
"""print current video path"""
import vlc

if __name__ == "__main__":
    path = vlc.path()
    if path:
        print(path)
