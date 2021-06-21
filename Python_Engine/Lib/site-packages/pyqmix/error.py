#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from cffi import FFI

from . import config
from .tools import find_dll
from .headers import ERROR_HEADER


class QmixError(object):
    """
    Qmix SDK error messages.

    """
    def __init__(self, error_number):
        dll_dir = config.read_config().get('qmix_dll_dir', None)
        dll_filename = 'usl.dll'

        dll_path = find_dll(dll_dir=dll_dir, dll_filename=dll_filename)
        if dll_path is None:
            msg = 'Could not find the Qmix SDK DLL %s.' % dll_filename
            raise RuntimeError(msg)
        else:
            self.dll_path = dll_path

        self._ffi = FFI()
        self._ffi.cdef(ERROR_HEADER)
        self._dll = self._ffi.dlopen(self.dll_path)

        self.error_number = error_number
        self._error_code = self._ffi.new('TErrCode *')

    @property
    def error_code(self):
        self._error_code = hex(abs(self.error_number))
        return self._error_code

    @property
    def error_string(self):
        e = self.error_code
        s = self._dll.ErrorToString(int(e, 16))
        return self._ffi.string(s).decode('utf8')
