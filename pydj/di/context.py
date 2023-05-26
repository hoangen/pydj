import importlib
import inspect
from typing import Any, Dict, List
from xml.dom.minidom import Document

from pydj.utils import find_modules, get_cls_from_name, get_cls_name

from .bean import Bean, Property, PropertyType, Scope
from .globals import registry
from .ref import ClsRef


class ApplicationContext:
    """
    Application Context for storing beans

    modules: list of modules for component scan
    """

    def __init__(self, modules: List[str] = ['.']):
        self._cls_beans: Dict[str, Bean] = {}
        self._singleton_cache: Dict[str, Any] = {}

        self._modules = modules
        self._scan_components(modules)

        self._register_beans()

    def get_bean(self, cls: type):
        cls_name = get_cls_name(cls)
        return self._instance(cls_name)

    def _get_bean(self, cls) -> Bean:
        return self._cls_beans[cls]

    def _get_beans(self) -> List[Bean]:
        return list(self._cls_beans.values())

    def _scan_components(self, modules_path: List[str]):
        discovered_modules = []
        for path in modules_path:
            discovered_modules.extend(find_modules(path))

        for module in discovered_modules:
            importlib.import_module(module)

    def _register_beans(self):
        for ri in registry:
            cls_name = get_cls_name(ri.cls)
            params = self._build_params(ri.cls)
            self._add_bean(cls_name, params, ri.scope)

    def _build_params(self, cls: type):
        sig = inspect.signature(cls)
        def_params = list(sig.parameters.values())
        params: List[Property] = []
        for dp in def_params:
            if dp.default is not sig.empty:
                params.append(
                    Property(name=dp.name, type=PropertyType.Const, value=dp.default))
            else:
                if dp.annotation in (int, float, str, list, set, dict, tuple):
                    raise ValueError(
                        "Basic type params must have default value or defined in consts.")
                else:
                    annotation_name = get_cls_name(dp.annotation)
                    params.append(
                        Property(name=dp.name, type=PropertyType.Ref, value=ClsRef(annotation_name)))
        return params

    def _add_bean(self, cls: str, params: List[Property], scope: Scope):
        bean = Bean(cls=cls,
                    params=params,
                    scope=scope)
        self._cls_beans[cls] = bean

    def _instance(self, cls: str):
        bean = self._get_bean(cls)
        existing_instance = self._get_bean_cache(bean)
        if bean.scope == Scope.SINGLETON and existing_instance:
            return existing_instance

        actual_params: Dict[str, Any] = {}
        for p in bean.params:
            if p.type == PropertyType.Const:
                actual_params[p.name] = p.value
            elif p.type == PropertyType.Ref:
                actual_params[p.name] = self._instance(p.value.target)
            else:
                raise ValueError(f'Unkown PropertyType {p.type}')

        ins = get_cls_from_name(bean.cls)(**actual_params)
        self._add_bean_cache(bean, ins)
        
        return ins

    def _get_bean_cache(self, bean: Bean):
        return self._singleton_cache.get(bean.cls, None)

    def _add_bean_cache(self, bean: Bean, ins: Any):
        self._singleton_cache[bean.cls] = ins

    def __str__(self) -> str:
        # format to xml by default
        return self.xml()

    def xml(self):
        doc = Document()
        beans_ele = doc.createElement('beans')
        for bean in self._get_beans():
            beans_ele.appendChild(bean.xml())
        doc.appendChild(beans_ele)
        return doc.toprettyxml()
