"""
prawo zipfa
proszę stworzyć listę frekwencyjną słów w tekście dla pliku pap.txt
"""

from collections import Counter
import re
from clp3 import clp


def lista_frekwencyjna(plik):
    with open(plik, "r", encoding="utf-8") as f:
        tekst = f.read().lower()
    # usunięcie znaków niealfabetycznych
    czysty_tekst = re.sub(r"[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]", "", tekst)

    slowa = czysty_tekst.split()
    #licznik = Counter(slowa)


    slowa_znorm = []
    for s in slowa:
        ids = clp.rec(s)
        if ids:
            podstawowa_forma = clp.bform(ids[0])
            slowa_znorm.append(podstawowa_forma)
        else:
            slowa_znorm.append(s)

    licznik = Counter(slowa_znorm)
    
    do_usuniecia = ["w", "i", "na", "z"]
    for word in do_usuniecia:
        licznik.pop(word, None)

    lista = licznik.most_common()
    return lista


plik = "pap.txt"
lista = lista_frekwencyjna(plik)
    
with open("output.txt", "w", encoding="utf-8") as f:
    for slowo, liczba in lista:
        ids = clp.rec(slowo)
        if ids:
            label = clp.label(ids[0])
        else:
            label = "-"
        f.write(f"{slowo}: {liczba} | {label}\n")
print("TEST")
