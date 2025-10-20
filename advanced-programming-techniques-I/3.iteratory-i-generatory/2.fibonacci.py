"""
Proszę napisać generator fibonacci(n), który zwraca kolejne liczby Fibonacciego aż do n.
"""

def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        temp = a
        a = b
        b = temp + b

for n in fibonacci(15):
    print(n)