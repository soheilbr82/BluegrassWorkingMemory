#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import applescript


@public.add
def playing():
    """return True if vk.com music is playing"""
    return bool(applescript.tell.app("Google Chrome", """
repeat with w in every window
    repeat with t in every tab of w
        if "https://vk.com/" is in (get URL of t) then
            tell t to set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_playing'),function(elem){return true;})"
            if (is_playing) then return true
        end if
    end repeat
end repeat
""").out)


def _toggle():
    return bool(applescript.tell.app("Google Chrome", """
repeat with w in every window
    repeat with t in every tab in w
        if "https://vk.com/" is in (get URL of t) then
           tell t to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_page_player_play'),function(elem){elem.click();})"
        end if
    end repeat
end repeat
"""))


@public.add
def pause():
    """pause vk.com music"""
    if playing():
        _toggle()


@public.add
def play():
    """continue play vk.com music"""
    if not playing():
        _toggle()
