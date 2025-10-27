"""
Proszę przygotować dekorator @memorize, który zapamiętuje wyniki wywołań funkcji dla danych argumentów.
Jeżeli funkcja zostanie wywołana ponownie z tymi samymi argumentami, dekorator powinien zwrócić wcześniej zapamiętany wynik, zamiast ponownie wykonywać obliczenia

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

