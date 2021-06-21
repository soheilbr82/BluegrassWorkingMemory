#!/usr/bin/env python
"""print `true` if fullscreen detected, else `false`"""
import google_chrome

if __name__ == "__main__":
    fullscreen = google_chrome.fullscreen.detect()
    print("true") if fullscreen else print("false")
