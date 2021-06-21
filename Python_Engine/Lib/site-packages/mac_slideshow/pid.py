#!/usr/bin/env python
"""print screensaver pid"""
import mac_screensaver

if __name__ == "__main__":
    pid = mac_screensaver.pid()
    if pid:
        print(pid)
