"""
- `statystyka.py` – funkcja obliczająca średnią i medianę z kolumny liczbowej.
"""

def srednia(kolumna):
    """Oblicza średnią arytmetyczną z listy liczb."""
    if not kolumna:
        return 0
    return sum(kolumna) / len(kolumna)

def mediana(kolumna):
    """Oblicza medianę z listy liczb."""
    n = len(kolumna)
    if n == 0:
        return 0
    posortowana = sorted(kolumna)
    srodek = n // 2
    if n % 2 == 1:
        return posortowana[srodek]
    else:
        return (posortowana[srodek - 1] + posortowana[srodek]) / 2
    
