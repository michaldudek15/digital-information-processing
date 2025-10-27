"""
Proszę przygotować dekorator @memorize, który zapamiętuje wyniki wywołań funkcji dla danych argumentów.
Jeżeli funkcja zostanie wywołana ponownie z tymi samymi argumentami, dekorator powinien zwrócić wcześniej 
zapamiętany wynik, zamiast ponownie wykonywać obliczenia

- wykorzystuje słownik (dict) jako pamięć podręczną (cache),
- kluczem jest krotka argumentów (args),
- przed obliczeniem sprawdza, czy wynik znajduje się już w pamięci.

@memorize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

Proszę zmierzyć czas działania funkcji fib(35) z dekoratorem i bez niego, aby zaobserwować różnicę.
"""
import time

def memorize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memorize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

start_time = time.time()
print(fib(35))
end_time = time.time()
print(f"czas wykonania z dekoratorem: {end_time - start_time:.6f} sekundy")

def fib_no_memory(n):
    if n < 2:
        return n
    return fib_no_memory(n-1) + fib_no_memory(n-2)
start_time = time.time()
print(fib_no_memory(35))
end_time = time.time()
print(f"czas wykonania bez dekoratora: {end_time - start_time:.6f} sekundy")


