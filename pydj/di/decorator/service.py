import logging

from . import component


class service(component):
    """service decorator"""

    def __init__(self, scope: str = "singleton"):
        super().__init__(scope)

    def __call__(self, cls: type):
        logging.debug(
            f'calling service decorator for class {cls}')
        return super().__call__(cls)
