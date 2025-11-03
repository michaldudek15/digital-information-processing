"""
- `csvtools.py` – funkcja wczytująca plik CSV i zwracająca listę słowników,
"""

import csv

def csvtools(nazwa_pliku):
    """Wczytuje plik CSV i zwraca listę słowników reprezentujących wiersze."""
    with open(nazwa_pliku, mode='r', newline='', encoding='utf-8') as plik:
        czytnik = csv.DictReader(plik)
        dane = [wiersz for wiersz in czytnik]
    return dane