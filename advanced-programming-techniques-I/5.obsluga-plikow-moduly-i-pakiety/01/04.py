"""
Proszę napisać funkcję, która przyjmie nazwę pliku i słowo kluczowe,
a następnie wyświetli wszystkie wiersze zawierające to słowo.
"""

def wyszukaj_wiersze_ze_slowem_kluczowym(nazwa_pliku, slowo_kluczowe):
    with open(nazwa_pliku, "r") as plik:
        for wiersz in plik:
            if slowo_kluczowe in wiersz:
                print(wiersz, end='')

nazwa_pliku = input("Podaj nazwę pliku do przeszukania: ")
slowo_kluczowe = input("Podaj słowo kluczowe do wyszukania: ")

wyszukaj_wiersze_ze_slowem_kluczowym(nazwa_pliku, slowo_kluczowe)   

