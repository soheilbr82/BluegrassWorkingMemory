#!/usr/bin/env python
"""print `true` if fullscreen mode detected"""
import vlc

if __name__ == "__main__":
    if vlc.fullscreen.detect():
        print("true")
