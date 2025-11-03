"""
Proszę rozbudować pakiet `analiza`, dodając moduł `raport.py`,

który wewnętrznie zaimportuje statystyka przez import względny.

Program główny ma wygenerować raport tekstowy z wynikami obliczeń.
"""

import analiza.raport as raport

nazwa_pliku_csv = "dane.csv"
from analiza.csvtools import csvtools
dane = csvtools(nazwa_pliku_csv)

if dane:
    kolumna_liczb = [float(wiersz['liczba']) for wiersz in dane if 'liczba' in wiersz]
    raport = raport.generuj_raport(kolumna_liczb)
    print(raport)
else:
    print("Brak danych do analizy.")

