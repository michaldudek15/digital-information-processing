"""
Proszę napisać własny iterator EvenNumbers, który zwraca parzyste liczby z określonego zakresu.

Przykład użycia:

for n in EvenNumbers(2, 10):
    print(n)
# Wynik: 2 4 6 8 10
"""

class EvenNumbers:
    def __init__(self, start, end):
        if start % 2 == 0:
            self.current = start
        else:
            self.current = start + 1
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


for i in EvenNumbers(2, 10):
    print(i)