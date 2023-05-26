import logging


class rest:
    def __init__(self, path='/'):
        self.path = path

    def __call__(self, cls):
        logging.debug(
            f'calling rest decorator for class {cls} with path {self.path}')
        return cls
