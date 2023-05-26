from typing import Any, Dict, List, Optional, Union

from pydj.di.gobal import beans_groups
from pydj.di.internal.ref import Ref
from pydj.di.internal.register_info import RegisterInfo


class component:
    """component decorator"""

    def __init__(self,
                 id: Optional[Union[str, type]] = None,
                 singleton: bool = True,
                 refs: Optional[Dict[str, Ref]] = None,
                 consts: Optional[Dict[str, Any]] = None,
                 group: str = 'default'
                 ):
        self.id = id
        self.singleton = singleton
        self.refs = refs
        self.consts = consts
        self.group = group

    def __call__(self, cls: type):
        print(
            f'calling component decorator for class {cls}')
        if type(self.id) is type:
            self.collect(id=None, cls=id)
            return id
        return cls

    def collect(self, id: Optional[str], cls: type):
        beans_groups.setdefault(self.group, []).append(RegisterInfo(
            id=id, singleton=self.singleton, refs=self.refs, consts=self.consts, cls=cls
        ))
