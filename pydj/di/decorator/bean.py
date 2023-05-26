import logging

class bean:
    """bean decorator"""

    def __init__(self):
        pass

    def __call__(self, func, *args, **kwargs):
        logging.debug(
            f'calling bean decorator for function {func} with params {args}')
