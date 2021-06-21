#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyqmix configuration.
"""

import os
from collections import OrderedDict
from ruamel.yaml import YAML
from appdirs import user_config_dir

yaml = YAML()
yaml.default_flow_style = False


PYQMIX_CONFIG_DIR = user_config_dir(appname='pyqmix', appauthor=False)
PYQMIX_CONFIG_FILE = os.path.join(PYQMIX_CONFIG_DIR, 'config.yaml')

DEFAULT_CONFIGS_DIR = os.path.normpath('C:/Users/Public/Documents/'
                                       'QmixElements/Projects/default_project/'
                                       'Configurations')

# Python 2 compatibility
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


def read_config():
    """
    Read the currently stored pyqmix configuration from disk.

    Returns
    -------
    cfg : dict
        The loaded configuration.

    """
    try:
        with open(PYQMIX_CONFIG_FILE, 'r') as f:
            cfg = yaml.load(f)
    except FileNotFoundError:
        try:
            os.makedirs(PYQMIX_CONFIG_DIR)
        except OSError:
            if not os.path.isdir(PYQMIX_CONFIG_DIR):
                raise

        cfg = OrderedDict([('qmix_dll_dir', ''),
                           ('qmix_config_dir', ''),
                           ('pumps', OrderedDict())])

    return cfg


def delete_config():
    """
    Delete the configuration file.

    """
    # Try to remove config file. Avoid error if the file has already
    # been deleted.
    try:
        os.remove(PYQMIX_CONFIG_FILE)
    except OSError:
        pass

    # Try to remove config directory. Only succeeds of directory
    # is empty.
    try:
        os.rmdir(PYQMIX_CONFIG_DIR)
    except OSError:
        pass


def get_available_qmix_configs(configs_dir=None):
    """
    Create a list of available qmix configurations

    Parameters
    ----------
    configs_dir : string or None
        The parent directory containing the Qmix configurations.
        If ``None``, assume the default directory used by
        Qmix Elements, i.e.,
        `C:/Users/Public/Documents/QmixElements/Projects/default_project/Configurations/`.

    Returns
    -------
    list of strings
        Names of available Qmix configurations.

    """
    if configs_dir is None:
        configs_dir = DEFAULT_CONFIGS_DIR

    def get_immediate_subdirectories(a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]

    return get_immediate_subdirectories(configs_dir)


def set_qmix_config(config_name, configs_dir=None):
    """
    Specify a Qmix configuration.

    Parameters
    ----------
    config_name : string
        The name of a Qmix configuration. Assumed to be stored at the default directory.
    configs_dir : string or None
        The parent directory containing the Qmix configurations.
        If ``None``, we will look for the Qmix configuration in the current
        directory; if not found, move on to look in the Qmix default
        directory.

    Raises
    ------
    ValueError
        If the specified configuration could not be found.

    """

    if configs_dir is None:
        if os.path.exists(config_name):
            configs_dir = os.path.abspath('.')
        else:
            configs_dir = DEFAULT_CONFIGS_DIR

    config_dir = os.path.join(configs_dir, config_name)

    if not os.path.exists(config_dir):
        msg = 'The specified configuration does not exist: %s' % config_dir
        raise ValueError(msg)

    cfg = read_config()
    cfg['qmix_config_dir'] = config_dir

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def set_qmix_dll_dir(d):
    """
    Specify the location of the directory containing the Qmix SDK DLL files.

    Parameters
    ----------
    d : string
        The Qmix SDK DLL directory. Must be an absolute path.

    """
    cfg = read_config()
    cfg['qmix_dll_dir'] = d

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def add_pump(index):
    """
    Add a new pump to the pyqmix configuration. Overwrites existing entries
    for a pump with the same index.

    Parameters
    ----------
    index : int
        The unique index of the pump. Indexing is zero-based, i.e. `index=0`
        refers to the first pump in the system.

    """
    if not isinstance(index, int):
        raise TypeError('Pump index must be an integer!')

    cfg = read_config()
    cfg['pumps'][index] = OrderedDict(
        [('name', None),
         ('volume_unit', None),
         ('flow_unit', None),
         ('syringe_params', None),
         ('drive_pos_counter', None)])

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def set_pump_name(index, name):
    """
    Set the name of a pump, as it will be stored in the configuration file.

    Parameters
    ----------
    index : int
        The index of the pump. Indexes are zero-based.

    index : str
        The desired name of the pump.

    """
    cfg = read_config()
    pump = cfg['pumps'][index]
    pump['name'] = name

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def set_pump_drive_pos_counter(index, value):
    """
    Set the pump drive position counter to the specified value.

    Parameters
    ----------
    index : int
        The index of the pump. Indexes are zero-based.

    value : float
        The value to set the drive position counter to.

    """
    cfg = read_config()
    pump = cfg['pumps'][index]
    pump['drive_pos_counter'] = value

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def set_pump_volume_unit(index, prefix, unit):
    """
    Set the pump volume unit.

    Parameters
    ----------
    index : int
        The index of the pump. Indexes are zero-based.

    prefix : str
        The prefix of the SIunit:
        ``centi``, ``deci``, ``mircro``, ``milli``, ``unit``.

    unit : str
        The volume unit identifier: ``litres``.

    """
    cfg = read_config()
    pump = cfg['pumps'][index]
    pump['volume_unit'] = OrderedDict([('prefix', prefix),
                                       ('unit', unit)])

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def set_pump_flow_unit(index, prefix, volume_unit, time_unit):
    """
    Set the flow unit for a certain pump.

    The flow unit defines the unit to be used for all flow values passed to
    API functions or retrieved from API functions.

    Parameters
    ----------
    prefix : str
        The prefix of the SI unit:
        ``centi``, ``deci``, ``milli``, ``micro``.

    volume_unit : str
        The volume unit identifier: ``litres``.

    time_unit : str
        The time unit (denominator) of the velocity unit:
        ``per_hour``, ``per_minute``, ``per_second``.

    """
    cfg = read_config()
    pump = cfg['pumps'][index]
    pump['flow_unit'] = OrderedDict([('prefix', prefix),
                                     ('volume_unit', volume_unit),
                                     ('time_unit', time_unit)])

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def set_pump_syringe_params(index, inner_diameter_mm, max_piston_stroke_mm):
    """
    Set syringe properties.

    If you change the syringe in one device, you need to setup the new
    syringe parameters to get proper conversion of flow rate und volume
    units.

    Parameters
    ----------
    inner_diameter_mm : float
        Inner diameter of the syringe tube in millimetres.

    max_piston_stroke_mm : float
        The maximum piston stroke defines the maximum position the piston
        can be moved to before it slips out of the syringe tube.
        The maximum piston stroke limits the maximum travel range of the
        syringe pump pusher.

    """
    cfg = read_config()
    pump = cfg['pumps'][index]
    pump['syringe_params'] = OrderedDict(
        [('inner_diameter_mm', inner_diameter_mm),
         ('max_piston_stroke_mm', max_piston_stroke_mm)])

    with open(PYQMIX_CONFIG_FILE, 'w') as f:
        yaml.dump(cfg, f)


def remove_pump(index):
    """
    Remove a pump and syringe configuration.

    Parameters
    ----------
    index : int
        The unique index of the pump.

    Raises
    ------
    KeyError
        If the specified pump index could not be found in the configuration
        file.

    """
    cfg = read_config()

    try:
        del cfg['pumps'][index]
        with open(PYQMIX_CONFIG_FILE, 'w') as f:
            yaml.dump(cfg, f)
    except KeyError:
        msg = ('Specified pump index could not be found in the configuration '
               'file.')
        raise KeyError(msg)
