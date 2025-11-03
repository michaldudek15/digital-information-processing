"""
Proszę napisać program, który otworzy plik `tekst.txt` i wypisze numerowaną listę wierszy:

```
1: To jest pierwszy wiersz
2: To jest drugi wiersz
```
"""

with open("tekst.txt", "r") as plik:
    for numer, wiersz in enumerate(plik, start=1):
        print(f"{numer}: {wiersz}", end='') 
