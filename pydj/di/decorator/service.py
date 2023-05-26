class service:
    """service decorator"""

    def __init__(self):
        pass

    def __call__(self, cls: type):
        print(
            f'calling service decorator for class {cls}')
        return cls
