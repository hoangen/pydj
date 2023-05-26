# import pkgutil

# absolute_modules = []

# def list_local_modules(package_name):
#     for module in pkgutil.walk_packages(path=None, prefix=package_name + '.'):
#         if module.ispkg:
#             print(f'{module.name} (package)')
#             list_local_modules(package_name + '.' + module.name)
#         else:
#             print(f'{module.name}')
#             absolute_modules.append(module.name)

# list_local_modules('pydj')


# # def find_modules(module_path):
# #     for package in pkgutil.walk_packages(module_path):
# #         print(package)
# #         if package.ispkg:
# #             find_modules([package.name])
# #         else:
# #             absolute_modules.append(package.name)

# # if __name__ == "__main__":
# #     find_modules('pydj')
# #     for module in absolute_modules:
# #         print(module)

import sys
from pkgutil import iter_modules

from setuptools import find_packages

from pydj.tools.decorator import debug


@debug
def find_modules(path):
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
    return modules


find_modules('app')
