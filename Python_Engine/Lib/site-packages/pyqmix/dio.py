#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from cffi import FFI

if sys.version_info[0] < 3:
    # Python 2 compatibility; requires `future` package.
    from builtins import bytes

from . import config
from .tools import CHK, find_dll
from .headers import DIGITAL_IO_HEADER


class QmixDigitalIO(object):
    """
    Qmix IO-B diglital I/O channel.

    """
    def __init__(self, index=None, name=''):
        """
        Parameters
        ----------
        index : int
            Index of the DIO channel. It is related with the config files.
            First channel has ``index=0``, second has ``index=1`` and so on.
            Takes precedence over the `name` parameter.

        name : str
            The name of the DIO channel to initialize. Will be ignored if `index` is
            not `None`.
        """
        if index is None and name == '':
            raise ValueError('Please specify a valid DIO index or name.')
        else:
            self.index = index
            self.name = name

        dll_dir = config.read_config().get('qmix_dll_dir', None)
        dll_filename = 'labbCAN_DigIO_API.dll'

        dll_path = find_dll(dll_dir=dll_dir, dll_filename=dll_filename)
        if dll_path is None:
            msg = 'Could not find the Qmix SDK DLL %s.' % dll_filename
            raise RuntimeError(msg)
        else:
            self.dll_path = dll_path

        self._ffi = FFI()
        self._ffi.cdef(DIGITAL_IO_HEADER)
        self._dll = self._ffi.dlopen(self.dll_path)

        self._handle = self._ffi.new('dev_hdl *', 0)

        if self.index is not None:
            self._call('LCDIO_GetOutChanHandle', self.index, self._handle)
        else:
            self._call('LCDIO_LookupOutChanByName',
                       bytes(self.name, 'utf8'),
                       self._handle)

    def _call(self, func_name, *args):
        func = getattr(self._dll, func_name)
        r = func(*args)
        return CHK(r)

    @property
    def is_output_on(self):
        """
        Current state of a digital output channel.

        Returns
        -------
        int
           1	Channel is ON
           0	Channel is OFF

        """
        r = self._call('LCDIO_IsOutputOn', self._handle[0])
        return bool(r)

    def write(self, state):
        """
        Swicth digital output channel on/off.

        Parameters
        ----------
        state : int
            State to set 0 = switch off, 1 = switch on.

        """
        self._call('LCDIO_WriteOn', self._handle[0], state)
