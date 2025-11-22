"""
```
analiza_tekstu/
├── __init__.py
├── wejscie.py
├── statystyka.py
└── raport.py
```

Proszę:

- w `wejscie.py` umieścić funkcję odczytującą plik tekstowy,
- w `statystyka.py` funkcje obliczające liczbę słów i średnią długość słowa dla każdego z tekstów i ogólnie,
- w `raport.py` funkcję generującą raport z użyciem importów względnych.
"""

from raport import generuj_raport

sciezki = ["teksty.txt", "test.txt"]
print(generuj_raport(sciezki))