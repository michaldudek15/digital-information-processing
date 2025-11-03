"""
Proszę przygotować moduł `matematyka.py` z funkcjami:
- srednia(lista_liczb),
- wariancja(lista_liczb).

Proszę dodać docstringi do każdej funkcji i wyświetlić 
ich treść poleceniem help().
"""

def srednia(lista_liczb):
    """Zwraca średnią arytmetyczną z listy liczb."""
    if not lista_liczb:
        return 0
    return sum(lista_liczb) / len(lista_liczb)

def wariancja(lista_liczb):
    """Zwraca wariancję z listy liczb."""
    if not lista_liczb:
        return 0
    avg = srednia(lista_liczb)
    return sum((x - avg) ** 2 for x in lista_liczb) / len(lista_liczb)

