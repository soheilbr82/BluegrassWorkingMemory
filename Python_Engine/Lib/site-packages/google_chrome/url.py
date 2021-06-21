#!/usr/bin/env python
"""print current url"""
import google_chrome

if __name__ == "__main__":
    url = google_chrome.url()
    if url:
        print(url)
