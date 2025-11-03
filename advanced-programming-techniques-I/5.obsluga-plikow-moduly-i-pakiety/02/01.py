"""
Proszę utworzyć plik osoby.csv z kolumnami: Imię, Nazwisko, Wiek.

Program ma odczytać dane, wypisać wszystkie wiersze i obliczyć 
średni wiek osób.
"""

import csv

with open("osoby.csv", "r") as plik:
    czytnik = csv.DictReader(plik, delimiter=';')
    suma_wiekow = 0
    liczba_osob = 0

    print("Dane osób:")
    for wiersz in czytnik:
        print(f"{wiersz['Imię']} {wiersz['Nazwisko']}, Wiek: {wiersz['Wiek']}")
        suma_wiekow += int(wiersz['Wiek'])
        liczba_osob += 1

    if liczba_osob > 0:
        sredni_wiek = suma_wiekow / liczba_osob
        print(f"\nŚredni wiek osób: {int(sredni_wiek)}")
    else:
        print("\nBrak danych o osobach.")

