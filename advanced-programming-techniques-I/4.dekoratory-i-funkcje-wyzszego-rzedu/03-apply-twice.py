"""
Proszę przygotować funkcję apply_twice(func, x), która przyjmuje jako argument inną funkcję oraz dowolną wartość, 
a następnie zwraca wynik dwukrotnego zastosowania tej funkcji do przekazanej wartości.

print(apply_twice(lambda x: x * 2, 3))    # 12, bo 3*2*2
print(apply_twice(lambda x: x**2, 2))       # 16, bo (2^2)^2
"""

def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda x: x * 2, 3))    # 12, bo 3*2*2
print(apply_twice(lambda x: x**2, 2))       # 16, bo (2^2)^2
