class bean:
    """bean decorator"""

    def __init__(self):
        pass

    def __call__(self, func, *args, **kwargs):
        print(
            f'calling bean decorator for function {func} with params {args}')
