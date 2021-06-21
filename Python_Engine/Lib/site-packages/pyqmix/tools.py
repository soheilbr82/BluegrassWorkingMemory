#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def CHK(return_code, *args):
    """
    Check if the return value of the invoked function returned an error.

    The Qmix DLL makes this pretty easy: All errors are indicated by
    negative return values.

    Parameters
    ----------
    return_code : int
        The code returned from a Qmix DLL function.
    args
        All arguments passed to the function ``funcname``.

    Returns
    -------
    return_code : int
        If no error occurred, the originally passed return value is
        returned.

    Raises
    ------
    RuntimeError
        If the DLL function returned an error code.

    """
    if return_code >= 0:
        return return_code
    else:
        from .error import QmixError  # We import here to avoid circularity with error.py
        e = QmixError(return_code)
        error_string = e.error_string
        msg = (error_string + ", Error number: " + str(e.error_number) +
               ", Error code: " + str(e.error_code))
        raise RuntimeError(msg)


def find_dll(dll_dir, dll_filename):
    """
    Try to find the specified DLL.

    If a DLL directory was given, try to find the DLL there.

    If no DLL directory was given, start looking for the DLL in the following
    order:

    - current working directory
    - global DLL search paths (this also respects the PATH
      environment variable)
    - default Qmix SDK installation directory

    Parameters
    ----------
    dll_dir : string or None
        The directory containing the DLLs. Pass `None` to look in the default locations.
    dll_filename : string
        The name of the DLL to find, including filename extension.

    Returns
    -------
    dll_path : string or None
        The path of the DLL, or `None` if the DLL could not be found.

    """
    if not dll_dir:
        # Check current directory.
        if os.path.exists(dll_filename):
            dll_path = dll_filename
            return dll_path

        # Check DLL search paths.
        import win32api
        try:
            win32api.LoadLibrary(dll_filename)
            dll_path = dll_filename
            return dll_path
        except Exception:
            pass

        # Check default installation directory.
        import appdirs
        dll_dir = appdirs.user_data_dir('QmixSDK', '')
        if os.path.exists(os.path.join(dll_dir, dll_filename)):
            dll_path = os.path.join(dll_dir, dll_filename)
            # Add DLL dir to PATH, otherwise we won't be able to load the DLL.
            os.environ['PATH'] += os.pathsep + dll_dir
            return dll_path

        return None
    else:
        if os.path.exists(os.path.join(dll_dir, dll_filename)):
            dll_path = os.path.join(dll_dir, dll_filename)
            # Add DLL dir to PATH, otherwise we won't be able to load the DLL.
            os.environ['PATH'] += os.pathsep + dll_dir
            return dll_path
        else:
            return None

