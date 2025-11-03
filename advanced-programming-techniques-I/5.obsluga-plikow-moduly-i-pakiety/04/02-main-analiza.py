"""
Proszę utworzyć pakiet `analiza` z modułami:

- `csvtools.py` – funkcja wczytująca plik CSV i zwracająca listę słowników,
- `statystyka.py` – funkcja obliczająca średnią i medianę z kolumny liczbowej.

Program `main.py` ma użyć tych modułów do analizy danych z pliku CSV.
"""

from analiza.csvtools import csvtools
from analiza.statystyka import srednia, mediana

nazwa_pliku_csv = "dane.csv"
dane = csvtools(nazwa_pliku_csv)

if dane:
    kolumna_liczb = [float(wiersz['liczba']) for wiersz in dane if 'liczba' in wiersz]
    print("Średnia:", srednia(kolumna_liczb))
    print("Mediana:", mediana(kolumna_liczb))
else:
    print("Brak danych do analizy.")
