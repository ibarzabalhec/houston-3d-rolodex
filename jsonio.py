# -*- coding: utf-8 -*-
"""Read and write the build's JSON files.

One place for the two things every call site used to repeat, and several
missed: the file is UTF-8, and it is closed when the call returns.
"""
import json


def read(path):
    """The JSON value in the file at `path`."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write(obj, path, **kw):
    """Write `obj` to `path` as JSON. Keyword arguments go to json.dump."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, **kw)
