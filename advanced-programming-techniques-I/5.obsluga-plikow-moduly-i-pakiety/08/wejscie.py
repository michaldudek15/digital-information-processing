def wczytaj_plik(sciezka):
    """Wczytuje plik tekstowy i zwraca jego zawartość jako string."""
    with open(sciezka, "r", encoding="utf-8") as f:
        return f.read()