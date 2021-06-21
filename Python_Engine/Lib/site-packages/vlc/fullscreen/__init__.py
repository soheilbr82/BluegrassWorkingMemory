#!/usr/bin/env python
import public
import vlc


@public.add
def detect():
    """return True if fullscreen mode detected"""
    return "true" in vlc.tell("fullscreen mode")


@public.add
def enter():
    """enter VLC fullscreen mode"""
    vlc.tell("set fullscreen mode to true")


@public.add
def exit():
    """exit VLC fullscreen mode"""
    vlc.tell("set fullscreen mode to false")
