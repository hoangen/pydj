import logging
from typing import Any, Dict, List, Optional, Union

from pydj.di.bean import RegisterInfo, Scope
from pydj.di.globals import registry


class component:
    """component decorator"""

    def __init__(self, scope: str = 'singleton'):
        self.scope = Scope[scope.upper()]

    def __call__(self, cls: type):
        logging.debug(
            f'calling component decorator for class {cls}')
        registry.append(RegisterInfo(cls=cls, scope=self.scope))
        return cls
