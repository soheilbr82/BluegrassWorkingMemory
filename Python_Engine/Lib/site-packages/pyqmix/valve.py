#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from cffi import FFI

if sys.version_info[0] < 3:
    # Python 2 compatibility; requires `future` package.
    from builtins import bytes

from . import config
from .dio import QmixDigitalIO
from .tools import CHK, find_dll
from .headers import VALVE_HEADER


class QmixValve(object):
    """
    Qmix valve interface.

    Parameters
    ----------
    index : int, or None
        Index of the valve to initialize. Takes precedence over the
        `name` and `handle` parameters.

    name : str
        The name of the valve to initialize. Will be ignored if `index` is
        not `None`. Takes precedence over the `handle` parameter.

    handle :  Qmix valve handle, or None
        A Qmix valve device handle, as returned by
        :func:~`pyqmix.QmixPump.valve_handle`.

    """
    def __init__(self, index=None, name='', handle=None):
        if index is None and name == '' and handle is None:
            raise ValueError('Please specify a valid valve index or name.')
        else:
            self.index = index
            self.name = name
            self.handle = handle

        dll_dir = config.read_config().get('qmix_dll_dir', None)
        dll_filename = 'labbCAN_Valve_API.dll'

        dll_path = find_dll(dll_dir=dll_dir, dll_filename=dll_filename)
        if dll_path is None:
            msg = 'Could not find the Qmix SDK DLL %s.' % dll_filename
            raise RuntimeError(msg)
        else:
            self.dll_path = dll_path

        self._ffi = FFI()
        self._ffi.cdef(VALVE_HEADER)
        self._dll = self._ffi.dlopen(self.dll_path)

        if self.index is not None:
            self._handle = self._ffi.new('dev_hdl *', 0)
            self._call('LCV_GetValveHandle', self.index, self._handle)
        elif self.name != '':
            self._call('LCV_LookupValveByName',
                       bytes(self.name, 'utf8'),
                       self._handle)
        else:
            self._handle = handle

        self.aspirate_pos = 1
        self.dispense_pos = 0

        self.name = name

    def _call(self, func_name, *args):
        func = getattr(self._dll, func_name)
        r = func(*args)
        return CHK(r)

    @property
    def number_of_positions(self):
        """
        Return the number of valve positions.

        Each valve has a number of available valve positions.
        A switching valve has two positions.

        Returns
        -------
        int
           >0 Number of valve positions

        """
        return self._call('LCV_NumberOfValvePositions', self._handle[0])

    @property
    def position(self):
        """
        The current logical valve position.

        Each valve position is identified by a logical valve position identifier
        from 0 to number of valve positions - 1. This function returns the
        logical valve position identifier for the current valve position.

        Returns
        -------
        int
           >=0 current valve position index.

        """
        return self._call('LCV_ActualValvePosition', self._handle[0])

    @position.setter
    def position(self, position):
        self.switch_position(position)

    def switch_position(self, position=None):
        """
        Switch the valve to a certain logical valve position.

        Parameters
        ----------
        position : int, or None
            Switch the valve to the specified position.
            If `None` and a valve with two possible positions is connected,
            switch from the current position to the other one.

        """
        if position is None and self.number_of_positions != 2:
            msg = ('For valves with more than 2 positions, please specify the '
                   'desired target position.')
            raise ValueError(msg)

        if position is None:
            if self.position == 0:
                target_position = 1
            else:
                target_position = 0
        else:
            target_position = position

        if ((target_position < 0) or
                (target_position >= self.number_of_positions)):
            msg = ('Must specify position in the range [0, %i] for this valve.'
                   % (self.number_of_positions - 1))
            raise ValueError(msg)

        self._call('LCV_SwitchValveToPosition', self._handle[0],
                   target_position)


class QmixExternalValve(QmixValve):
    """
    An external valve, controlled by Qmix I/O-B.

    Parameters
    ----------
    index : int, or None
        Index of the DIO channel to istantiate. Takes precedence over the
        `name` parameter.

    name : str
        The name of the DIO channel to initialize. Will be ignored if `index` is
        not `None`.

    """
    def __init__(self, index=None, name=''):
        if index is None and name == '':
            raise ValueError('Please specify a valid DIO index or name')
        else:
            self.index = index
            self.name = name

        if self.index is not None:
            self._dio = QmixDigitalIO(index=self.index)
        else:
            self._dio = QmixDigitalIO(name=self.name)

        self.aspirate_pos = 1
        self.dispense_pos = 0

    @property
    def number_of_positions(self):
        return 2

    @property
    def position(self):
        """
        The current logical valve position.

        Each valve position is identified by a logical valve position identifier
        from 0 to number of valve positions - 1. This function returns the
        logical valve position identifier for the current valve position.

        Returns
        -------
        int
           >=0 current valve position index.

        """
        r = self._dio.is_output_on

        if r:
            return 1
        else:
            return 0

    @position.setter
    def position(self, position):
        self.switch_position(position)

    def switch_position(self, position=None):
        """
        Switch the valve to a certain logical valve position.

        Parameters
        ----------
        position : int, or None
            Switch the valve to the specified position.
            If `None` and a valve with two possible positions is connected,
            switch from the current position to the other one.

        """
        if position is None:
            if self.position == 0:
                target_position = 1
            else:
                target_position = 0
        else:
            target_position = position

        if ((target_position < 0) or
                (target_position >= self.number_of_positions)):
            msg = ('Must specify position in the range [0, %i] for this valve.'
                   % (self.number_of_positions - 1))
            raise ValueError(msg)

        self._dio.write(target_position)
