"""
Proszę napisać generator, który zwraca liczby od 1 do nieskończoności, ale zatrzymuje się, gdy suma przekroczy 100.
"""

def inf(limit):
    suma = 0
    n = 1
    while True:
        suma += n
        if suma > limit:
            break
        yield n
        n += 1

for n in inf(1000):
    print(n)