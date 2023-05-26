class get:
    def __init__(self, path='/'):
        self.path = path

    def __call__(self, func):
        print(
            f'calling get decorator for function {func} with path {self.path}')
