import importlib
import sys
from pkgutil import iter_modules
from typing import List

from setuptools import find_packages


def find_modules(path: str) -> List[str]:
    modules = []
    for pkg in find_packages(path):
        modules.append(pkg)
        pkgpath = path + '/' + pkg.replace('.', '/')
        if sys.version_info.major == 2 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.append(pkg + '.' + name)
        else:
            for info in iter_modules([pkgpath]):
                if not info.ispkg:
                    modules.append(pkg + '.' + info.name)
    if path != '.':
        modules = [path + '.' + module for module in modules]
    return modules


def get_cls_name(cls: type) -> str:
    return cls.__module__ + '.' + cls.__qualname__


def get_cls_from_name(cls_name: str) -> type:
    try:
        mod_path, name = cls_name.rsplit('.', 1)
        return getattr(importlib.import_module(mod_path), name)
    except ValueError:
        return getattr(importlib.import_module('__main__'), cls_name)


def add_two_numbers(a: int, b: int) -> int:
    return a + b
