"""
Celem projektu jest stworzenie zestawu dekoratorów, które pozwalają:
- rejestrować wywołania funkcji (nazwa, czas, argumenty, wynik),
- mierzyć czas działania funkcji,
- zliczać liczbę wywołań,
- oraz zapamiętywać wyniki obliczeń dla powtarzających się argumentów.

```
from decorators import log_call, measure_time, count_calls

@count_calls
@measure_time
@log_call("wyniki.log")
def fib(n):
    ...
```

```
Funkcja fib została wywołana 1 razy
Czas wykonania fib: 0.0001s
Funkcja factorial została wywołana 1 razy
Czas wykonania factorial: 0.0000s

wyniki.log
[2025-10-26 22:45:32] fib(5,) -> 5
[2025-10-26 22:45:33] factorial(5,) -> 120
```

Proszę zastosować dekoratory do kilku funkcji, np.:
- obliczanie silni (factorial),
- obliczanie Fibonacciego (fib),
- konwersja temperatur (to_celsius, to_fahrenheit).
"""
from decorators import log_call, measure_time, count_calls, memorize
import time

@count_calls
@measure_time
@log_call("wyniki.log")
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

@count_calls
@measure_time
@log_call("wyniki.log")
@memorize
def fib_memorized(n):
    if n <= 1:
        return n
    return fib_memorized(n - 1) + fib_memorized(n - 2)

@count_calls
@measure_time
@log_call("wyniki.log")
@memorize
def factorial_memorized(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

@count_calls
@measure_time
@log_call("wyniki.log")
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

@count_calls
@measure_time
@log_call("wyniki.log")
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

@count_calls
@measure_time
@log_call("wyniki.log")
def to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

@count_calls
@measure_time
def slow_function(x):
    time.sleep(2)
    return x * x    

if __name__ == "__main__":
    print(f"fib(5) = {fib(5)}")
    print(f"fib_memorized(5) = {fib_memorized(5)}")
    print(f"factorial(10) = {factorial(10)}")
    print(f"factorial_memorized(10) = {factorial_memorized(10)}")
    print(f"to_celsius(100) = {to_celsius(100)}")
    print(f"to_fahrenheit(0) = {to_fahrenheit(0)}")
    print(f"slow_function(4) = {slow_function(4)}")
    #print(f"slow_function(4) = {slow_function(4)}")