#!/usr/bin/env python
"""print `true` vk.com music os playing, else `false`"""
import mac_vk


def _cli():
    playing = mac_vk.playing()
    if playing:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    _cli()
