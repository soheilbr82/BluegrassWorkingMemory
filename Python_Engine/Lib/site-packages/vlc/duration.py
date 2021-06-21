#!/usr/bin/env python
"""print current video duration"""
import vlc

if __name__ == "__main__":
    duration = vlc.duration()
    if duration:
        print(duration)
