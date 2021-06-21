#!/usr/bin/env python
"""print tabs urls"""
import google_chrome

if __name__ == "__main__":
    urls = google_chrome.urls()
    if urls:
        print("\n".join(urls))
