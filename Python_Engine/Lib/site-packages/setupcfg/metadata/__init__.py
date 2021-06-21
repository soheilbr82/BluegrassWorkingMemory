#!/usr/bin/env pythons

"""
http://setuptools.readthedocs.io/en/latest/setuptools.html#metadata
key, alias
"""

ALIASES = [
    ("url", "home-page"),
    ("download_url", "download-url"),
    ("author_email", "author-email"),
    ("maintainer_email", "maintainer-email"),
    ("classifiers", "classifier"),
    ("description", "summary"),
    ("long_description", "long-description"),
    ("long_description_content_type", ""),
    ("platforms", "platform"),
]

KEYS = [
    "name",
    "version",
    "url",
    "download_url",
    "project_urls",
    "author",
    "author_email",
    "maintainer",
    "maintainer_email",
    "classifiers",
    "license",
    "description",
    "long_description",
    "long_description_content_type",
    "keywords",
    "platforms",
    "provides",
    "requires",
    "obsoletes",
]


def _aliaskv(key, value):
    for aliaskey, alias in ALIASES:
        if key == alias:
            key = aliaskey
    return key, value


def _aliasdict(*args, **kwargs):
    inputdict = dict(*args, **kwargs)
    resultdict = dict()
    for key, value in inputdict.items():
        key, value = _aliaskv(key, value)
        resultdict[key] = value
    return resultdict
