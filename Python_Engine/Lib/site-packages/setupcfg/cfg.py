#!/usr/bin/env python
import collections
try:
    from ConfigParser import ConfigParser
    import StringIO
except ImportError:
    from configparser import ConfigParser  # python3
    import io
import setupcfg
import orderdict
import write

"""
http://setuptools.readthedocs.io/en/latest/setuptools.html#metadata
http://setuptools.readthedocs.io/en/latest/setuptools.html#options
"""

SECTIONS = ["metadata", "options"]


def _dict2configparser(*args, **kwargs):
    """
python2.X dict ordering not supported (use collections.OrderedDict)
configparser.update(dict) python3 only
    """
    inputdict = collections.OrderedDict(*args, **kwargs)
    configparser = ConfigParser()
    for section, value in inputdict.items():
        configparser.add_section(section)
        for k, v in value.items():
            configparser.set(section, k, v)
    return configparser


def _strings(data):
    result = collections.OrderedDict()
    for key, value in data.items():
        if value is not None:
            value = setupcfg.values.string(value)
            if value:
                result[key] = value
    return result


class Setupcfg(collections.defaultdict):
    """`setup.cfg` generator class. dict/attr access to sections dicts"""
    __readme__ = ["load", "save", "string"]

    def load(self, path="setup.cfg"):
        """load from `setup.cfg` file"""
        config = ConfigParser()
        config.read(path)
        for section in config.sections():
            if section not in self:
                self[section] = dict()
            for option, value in config.items(section):
                self[section][option] = setupcfg.values.value(value)
        return self

    def save(self, path="setup.cfg"):
        """save to `setup.cfg` file"""
        value = self.string()
        write.write(path, value)
        return self

    def _configparser(self):
        metadata = orderdict.order(setupcfg.metadata.KEYS, self.get("metadata", {}))
        options = orderdict.order(setupcfg.options.KEYS, self.get("options", {}))
        data = dict(self, metadata=metadata, options=options)
        for section_name, section_data in data.items():
            data[section_name] = _strings(section_data)
        data = orderdict.order(SECTIONS, data)
        return _dict2configparser(data)

    def string(self):
        """return string representation"""
        try:
            output = StringIO.StringIO()
        except NameError:
            output = io.StringIO()
        self._configparser().write(output)
        value = output.getvalue()
        output.close()
        return value

    def __getattr__(self, attr):
        """return dictionary with section data"""
        if attr in self:
            return self[attr]

    def __missing__(self, key):
        self[key] = dict()
        return self[key]

    def __setitem__(self, key, value):
        if not isinstance(value, dict):
            raise ValueError("'%s' is not dict" % key)
        super(type(self), self).__setitem__(key, value)

    def __str__(self):
        return self.string()
