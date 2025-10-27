"""
Proszę utworzyć funkcję licznik(start), która zwraca funkcję wewnętrzną zwiększającą licznik przy każdym wywołaniu.

c = licznik(10)
print(c())  # 11
print(c())  # 12
"""

def licznik(start):
    counter = start
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

c = licznik(10)
print(c())  # 11
print(c())  # 12
