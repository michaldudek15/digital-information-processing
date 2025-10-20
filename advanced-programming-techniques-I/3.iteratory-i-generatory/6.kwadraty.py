"""
Proszę użyć generator expression, by obliczyć sumę kwadratów liczb od 1 do 100, bez tworzenia pełnej listy.
"""

# gen = (x * x for x in range(5))

kwadraty = sum(x * x for x in range(1, 5))
print(kwadraty)