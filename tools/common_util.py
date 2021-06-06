import os
import sys
import uuid
import platform
import importlib
import hashlib
import json
from datetime import datetime


class DotDict(dict):

    def __getattr__(self, attr):
        if attr.startswith('__'):
            raise AttributeError
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def base_module_path():
    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    return base_path


def current_module_name():
    module_file = os.path.basename(sys.argv[0])
    current_module = os.path.splitext(module_file)[0]
    return current_module


def osname():
    return platform.system().upper()


def current_time(utc=False):

    if utc is True:
        return datetime.utcnow().replace(microsecond=0)
    else:
        return datetime.now().replace(microsecond=0)


def json_encode(data):
    return json.dumps(data).encode()


def json_decode(data):
    return json.loads(data.decode('utf-8'))
