#!/usr/bin/env python
import os
import public


DOMAIN = "com.apple.ScreenSaverPhotoChooser"


@public.add
def read(key):
    """return preferences value"""
    args = ["defaults", "-currentHost", "read", DOMAIN, key]
    return os.popen(" ".join(args)).read().strip()


@public.add
def write(key, value):
    """write preferences value"""
    old = read(key)
    if value != old:
        args = ["defaults", "-currentHost", "write", DOMAIN, key, str(value)]
        os.popen(" ".join(args))
        os.system(" ".join(["killall", "cfprefsd", "System Preferences"]))
