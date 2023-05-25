class Rest:
    """Decorator for a REST controller"""

    def __init__(self, cls):
        self.cls = cls

    def __call__(self):
        pass
