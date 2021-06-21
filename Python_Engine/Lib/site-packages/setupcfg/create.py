#!/usr/bin/env python
"""generate `setup.cfg`"""
import os
import sys
import setupcfg
import setuptools


def name():
    """return `name` string - working dir name without extension"""
    return os.path.basename(os.getcwd()).split(".")[0].lower()


def packages():
    """return `packages` list - `setuptools.find_packages()`"""
    return setuptools.find_packages()


def py_modules():
    """return list with python modules in project root"""
    def ismodule(f):
        return os.path.splitext(f)[1] == ".py" and f != "setup.py"

    def module_name(f):
        return os.path.splitext(f)[0]
    return list(map(module_name, filter(ismodule, os.listdir(os.getcwd()))))


def install_requires():
    """return `install_requires` list. content of `install_requires.txt`, `requirements.txt`, `requires.txt` files"""
    result = []
    files = ["install_requires.txt", "requirements.txt", "requires.txt"]

    def readline(l):
        return l.split("#")[0].lstrip().rstrip()
    for path in files:
        if os.path.exists(path):
            result += list(map(readline, open(path).read().splitlines()))
    return list(sorted(filter(None, set(result))))


def scripts():
    """return `scripts` list. `bin/`, `scripts/` files"""
    result = []
    exclude = ['.DS_Store', 'Icon\r']
    for path in ["bin", "scripts"]:
        if os.path.exists(path) and os.path.isdir(path):
            files = list(filter(lambda f: f not in exclude, os.listdir(path)))
            result += list(map(lambda f: os.path.join(path, f), files))
    return result


def _get_env(key):
    for _key in [key, key.upper()]:
        if _key in os.environ:
            return os.environ[_key]


def _env_data(keys):
    result = dict()
    for key in keys:
        value = _get_env(key)
        if value:
            result[key] = value
    return result


def metadata():
    data = dict(name=name())
    for key, path in [("classifiers", ""), ("description", ""), ("long_description", "README.md")]:
        path = path if path else "%s.txt" % key
        if os.path.exists(path):
            data[key] = "file: %s" % path
    if os.path.splitext(data.get("long_description", ""))[1] == ".md":
        data["long_description_content_type"] = "text/markdown"
    if os.path.exists("version.txt"):
        data["version"] = open("version.txt").read()
    data.update(_env_data(setupcfg.metadata.KEYS))
    return data


def options():
    return dict(
        install_requires=install_requires(),
        packages=packages(),
        py_modules=py_modules(),
        scripts=scripts()
    )


def _cli():
    if not os.path.exists("setup.py"):
        sys.exit("%s/setup.py not exists" % os.getcwd())
    cfg = setupcfg.Setupcfg(metadata=metadata(), options=options())
    print(str(cfg))


if __name__ == "__main__":
    _cli()
