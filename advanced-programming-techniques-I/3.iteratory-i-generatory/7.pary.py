"""
Proszę zaimplementować generator pairwise(iterable), który zwraca pary kolejnych elementów:

Np.

list(pairwise([10, 20, 30, 40]))  # [(10, 20), (20, 30), (30, 40)]
"""

def pairwise(iterable):
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return
    for current in it:
        yield (prev, current)
        prev = current

print(list(pairwise([10, 20, 30, 40])))