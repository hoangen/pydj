import importlib
from typing import List

from pydj.di.utils import find_modules, get_cls_name


class ApplicationContext:
    """Application Context for storing beans

    modules: list of modules for component scan
    """

    def __init__(self, modules: List[str] = []):
        self.beans = {}
        self.modules = modules

        self.__scan_components(modules)

    def instance_by_cls(self, cls):
        return self.beans[cls]

    def __scan_components(self, modules_path):
        discovered_modules = []
        for path in modules_path:
            discovered_modules.extend(find_modules(path))

        for module in discovered_modules:
            importlib.import_module(module)

    def __str__(self) -> str:
        return '<beans><bean></bean></beans>'

     # def register_group(self, clses: List[type]):
    #     for cls in clses:
    #         cls_name = get_cls_name(cls)
    #         mod_path, name = cls_name.rsplit('.', 1)
    #         print(f"debug: mod_path={mod_path}, name={name}")
    #         instance = getattr(importlib.import_module(mod_path), name)(customer_service=CustomerService())
    #        self.beans[cls] = instance
