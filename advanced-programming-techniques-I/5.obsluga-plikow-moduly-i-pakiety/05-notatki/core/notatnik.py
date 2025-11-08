from .pliki import wczytaj_notatki, zapisz_notatki

def dodaj_notatke(tytul, tresc):
    notatki = wczytaj_notatki()
    nowa = {"tytul": tytul, "tresc": tresc}
    notatki.append(nowa)
    zapisz_notatki(notatki)


def wyszukaj_notatke(slowo_kluczowe):
    notatki = wczytaj_notatki()
    return [
        n for n in notatki
        if slowo_kluczowe.lower() in n["tytul"].lower() or slowo_kluczowe.lower() in n["tresc"].lower()
    ]

def usun_notatke(tytul):
    notatki = wczytaj_notatki()
    nowe_notatki = [n for n in notatki if n["tytul"] != tytul]
    if len(nowe_notatki) != len(notatki):
        zapisz_notatki(nowe_notatki)
        return True
    return False

def pokaz_wszystkie():
    return wczytaj_notatki()