def debug(func):
    def wrapper(*args, **kwargs):
        print(f'call {func.__name__}({args})')
        result = func(*args, **kwargs)
        print(f'return {func.__name__}: {result}')
        return result
    return wrapper
