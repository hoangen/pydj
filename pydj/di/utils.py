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

    modules = [path + '.' + module for module in modules]
    return modules


def get_cls_name(cls: type) -> str:
    return cls.__module__ + '.' + cls.__qualname__


def add_two_numbers(a: int, b: int) -> int:
    return a + b
