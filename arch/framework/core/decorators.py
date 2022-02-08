import time


def debug(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        print(f'Была вызвана функция {func.__name__}  '
              f'время выполнения - {time.time() - start_time}')
        return f

    return wrapper
