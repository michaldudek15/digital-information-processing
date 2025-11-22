from wejscie import wczytaj_plik
from statystyka import licz_slowa, srednia_dlugosc_slowa, statystyki_ogolne


def generuj_raport(lista_sciezek):
    """Generuje raport statystyczny dla podanych plików tekstowych."""
    teksty = [wczytaj_plik(s) for s in lista_sciezek]

    raport = []
    for sciezka, tresc in zip(lista_sciezek, teksty):
        raport.append(f"nazwa pliku: {sciezka}")
        raport.append(f"  - liczba słów: {licz_slowa(tresc)}")
        raport.append(f"  - średnia długość słowa: {srednia_dlugosc_slowa(tresc)}")
        raport.append("")

    # Statystyki ogólne
    og_liczba, og_srednia = statystyki_ogolne(teksty)
    raport.append("statystyki łączone:")
    raport.append(f"  - łączna liczba słów: {og_liczba}")
    raport.append(f"  - średnia długość słowa ogółem: {og_srednia}")

    return "\n".join(raport)