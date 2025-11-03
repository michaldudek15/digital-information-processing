"""
Proszę utworzyć plik `tekst.txt` z kilkoma wierszami tekstu.
Następnie proszę napisać program, który:

- otworzy plik,
- wyświetli jego zawartość na ekranie,
- policzy, ile wierszy znajduje się w pliku.
"""

with open("tekst.txt", "r") as plik:
    zawartosc = plik.read()
    print("zawartość pliku:")
    print(zawartosc)
    print("\nLiczba wierszy:", len(zawartosc.splitlines()))
