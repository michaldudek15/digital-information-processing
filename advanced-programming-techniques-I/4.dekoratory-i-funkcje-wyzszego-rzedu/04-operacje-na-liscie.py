"""
Proszę wykorzystać map, filter oraz reduce do operacji na liście numbers = [1, 2, 3, 4, 5, 6]:

- za pomocą map proszę utworzyć listę kwadratów.
- za pomocą filter proszę wybrać liczby parzyste.
- za pomocą reduce (z modułu functools) proszę obliczyć sumę wszystkich elementów.
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

kwadraty = list(map(lambda x: x**2, numbers))
print("kwadraty:", kwadraty)

liczby_parzyste = list(filter(lambda x: x % 2 == 0, numbers))
print("liczby parzyste:", liczby_parzyste)

suma = reduce(lambda x, y: x + y, numbers)
print("suma wszystkich elementów:", suma)
