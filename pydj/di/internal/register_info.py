from typing import Any, Dict, Optional

from pydj.di.internal.ref import Ref


class RegisterInfo:
    def __init__(self,
                 cls: type,
                 id: Optional[str] = None,
                 singleton: bool = True,
                 refs: Optional[Dict[str, Ref]] = None,
                 consts: Optional[Dict[str, Any]] = None):
        self.cls = cls
        self.id = id
        self.singleton = singleton
        self.refs = refs
        self.consts = consts
