"""
funkcja do zapisu do pliku
"""

def pisz(nazwa_pliku, zawartosc):
    """Zapisuje podaną zawartość do pliku o podanej nazwie."""
    with open(nazwa_pliku, "w") as plik:
        plik.write(zawartosc)
