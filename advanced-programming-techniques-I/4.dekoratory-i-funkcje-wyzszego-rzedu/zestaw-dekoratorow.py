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

