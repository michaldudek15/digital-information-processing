"""
Proszę rozbudować pakiet `analiza`, dodając moduł `raport.py`,

który wewnętrznie zaimportuje statystyka przez import względny.
"""

from .statystyka import srednia, mediana

def generuj_raport(kolumna_liczb):
    """Generuje raport tekstowy z wynikami obliczeń średniej i mediany."""
    avg = srednia(kolumna_liczb)
    med = mediana(kolumna_liczb)
    raport = f"Raport analizy danych:\nŚrednia: {avg}\nMediana: {med}\n"
    return raport