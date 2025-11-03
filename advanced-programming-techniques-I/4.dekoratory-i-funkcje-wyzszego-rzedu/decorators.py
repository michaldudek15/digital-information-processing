import datetime, functools

def log_call(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as f:
                f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__}{args} -> {result}\n")
            return result
        return wrapper
    return decorator

import time

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[TIME] Czas wykonania funkcji {func.__name__}: {elapsed_time:.4f} sekundy")
        return result
    return wrapper

def count_calls(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"[COUNT] Funkcja {func.__name__} została wywołana {count} razy.")
        return func(*args, **kwargs)
    return wrapper

def memorize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
