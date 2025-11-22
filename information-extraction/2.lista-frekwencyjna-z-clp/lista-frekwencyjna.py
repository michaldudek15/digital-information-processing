"""
prawo zipfa
proszę stworzyć listę frekwencyjną słów w tekście dla pliku pap.txt
"""

from collections import Counter
import re
# from clp3 import CLP

import sys
print(sys.path)


def lista_frekwencyjna(plik):
    with open(plik, "r", encoding="utf-8") as f:
        tekst = f.read().lower()
    # usunięcie znaków niealfabetycznych
    czysty_tekst = re.sub(r"[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]", "", tekst)

    slowa = czysty_tekst.split()
    licznik = Counter(slowa)
    
    do_usuniecia = ["w", "i", "na", "z"]
    for word in do_usuniecia:
        licznik.pop(word, None)

    lista = licznik.most_common()
    return lista

if __name__ == "__main__":
    plik = "pap.txt"
    lista = lista_frekwencyjna(plik)
    #for slowo, liczba in lista:
    #    print(f"{slowo}: {liczba}")

    # zapisanie outputu do pliku
    with open("output.txt", "w", encoding="utf-8") as f:
        for slowo, liczba in lista:
            f.write(f"{slowo}: {liczba}\n") 


