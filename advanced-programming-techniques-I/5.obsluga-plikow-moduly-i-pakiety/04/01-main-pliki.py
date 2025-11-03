"""
### Pakiet „pliki”

Proszę utworzyć katalog `pliki` z plikami:

- `__init__.py`
- `czytaj.py` (funkcja odczytu pliku)
- `pisz.py` (funkcja zapisu do pliku)


Proszę napisać skrypt `main.py`, który zaimportuje te 
funkcje i umożliwi użytkownikowi zapis i odczyt tekstu z pliku.
"""

from pliki.czytaj import czytaj
from pliki.pisz import pisz

nazwa_pliku = "przyklad.txt"
zawartosc_do_zapisu = "To jest przykładowy tekst do zapisu w pliku."

pisz(nazwa_pliku, zawartosc_do_zapisu)

zawartosc_plik = czytaj(nazwa_pliku)
print(zawartosc_plik)   

