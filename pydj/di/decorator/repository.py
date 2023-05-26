class repository:
    """repository decorator"""

    def __init__(self):
        pass

    def __call__(self, cls: type):
        print(
            f'calling repository decorator for class {cls}')
        return cls
