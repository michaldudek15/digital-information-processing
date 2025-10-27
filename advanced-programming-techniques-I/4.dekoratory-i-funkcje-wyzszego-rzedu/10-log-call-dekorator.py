"""
Proszę przygotować dekorator @log_call(filename), który zapisze do pliku informację o wywołaniu 
funkcji w formacie:
`[2025-10-26 20:15:02] add(2,3) -> 5`.

Proszę zastosować go do kilku różnych funkcji (np. add, multiply).
"""

import datetime

def log_call(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as f:
                f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__}{args} -> {result}\n")
            return result
        return wrapper
    return decorator

@log_call("10-log.txt")
def add(x, y):
    return x + y

@log_call("10-log.txt")
def multiply(x, y):
    return x * y

print(add(2, 3))
print(multiply(4, 5))
