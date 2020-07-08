from functools import wraps
from time import time


def record_time(func):
    # 自定義裝飾函數的裝飾器
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}:{time()-start}秒')
        return result
    return wrapper


def record(output):
    # 可參數化的裝飾器
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            print(f'{func.__name__}:{time()-start}秒')
            return result
        return wrapper
    return decorate


class Record():
    # 透過 class 定義裝飾器
    def __init__(self, output):
        self.output = output

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            print(f'{func.__name__}:{time()-start}秒')
            return result
        return wrapper
