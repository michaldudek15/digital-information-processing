def licz_slowa(tekst):
    """zwraca liczbę słów w tekście"""
    slowa = tekst.split()
    return len(slowa)


def srednia_dlugosc_slowa(tekst):
    """zwraca średnią długość słowa w tekście"""
    slowa = tekst.split()
    if not slowa:
        return 0
    dlugosci = [len(s) for s in slowa]
    return sum(dlugosci) / len(dlugosci)


def statystyki_ogolne(lista_tekstow):
    """zwraca ogólną liczbę słów i średnią długość słowa dla wielu tekstów"""
    wszystkie_slowa = []
    for tekst in lista_tekstow:
        wszystkie_slowa.extend(tekst.split())

    if not wszystkie_slowa:
        return 0, 0

    liczba = len(wszystkie_slowa)
    srednia = sum(len(s) for s in wszystkie_slowa) / liczba
    return liczba, srednia