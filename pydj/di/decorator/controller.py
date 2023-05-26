from . import component


class controller(component):
    """controller decorator"""

    def __init__(self, endpoint='/'):
        self.endpoint = endpoint

    def __call__(self, cls: type):
        print(
            f'calling controller decorator for class {cls} with endpoint {self.endpoint}')
        return cls
