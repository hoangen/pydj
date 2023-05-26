
import enum
import xml
from typing import Any, List, Union

from .ref import Ref


class Scope(str, enum.Enum):
    SINGLETON = "singleton"
    PROTOTYPE = "prototype"
    REQUEST = "request"
    SESSION = "session"
    APPLICATION = "application"
    WEBSOCKET = "websocket"


class RegisterInfo:
    def __init__(self,
                 cls: type,
                 scope: Scope = Scope.SINGLETON):
        self.cls = cls
        self.scope = scope

    def __str__(self) -> str:
        return f'RegisterInfo({self.cls}, {self.scope})'


class PropertyType(str, enum.Enum):
    Const = "const"
    Ref = "ref"


class Property:

    def __init__(self, name: str, type: PropertyType, value: Union[Any, Ref]):
        self.name = name
        self.type = type
        self.value = value

    def to_xml(self):
        elem = xml.dom.minidom.Document().createElement('property')
        elem.setAttribute("name", self.name)

        if self.type is PropertyType.Ref:
            elem.setAttribute("ref", self.value.to_expr())
        elif self.type is PropertyType.Const:
            elem.setAttribute("value", str(self.value))
            elem.setAttribute("value-type", type(self.value).__name__)
        else:
            raise ValueError("unknown property type")

        return elem

    def __repr__(self):
        return self.to_xml().toxml()


class Bean:
    def __init__(self,
                 cls: str,
                 params: List[Property],
                 scope: Scope):
        self.cls = cls
        self.params = params
        self.scope = scope
