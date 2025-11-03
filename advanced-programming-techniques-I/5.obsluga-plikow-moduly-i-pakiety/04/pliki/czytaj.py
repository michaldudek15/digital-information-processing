"""
funkcja do odczytu pliku
"""

def czytaj(nazwa_pliku):
    """Odczytuje zawartość pliku o podanej nazwie."""
    with open(nazwa_pliku, "r") as plik:
        zawartosc = plik.read()
    return zawartosc
