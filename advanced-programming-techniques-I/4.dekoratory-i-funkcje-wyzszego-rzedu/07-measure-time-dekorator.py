"""
Proszę przygotować dekorator @measure_time, który zmierzy i wypisze czas działania funkcji.

@measure_time
def slow_function():
    for _ in range(10**6):
        pass
"""

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[TIME] Czas wykonania funkcji {func.__name__}: {elapsed_time:.4f} sekundy")
        return result
    return wrapper

@measure_time
def slow_function():
    for _ in range(10**8):
        pass

slow_function()