def wyswietlMacierz(macierz):
        for wiersz in macierz:
            print(wiersz)

def levenshtein():
    pierwszeSlowo = input("pierwsze słowo: ")
    drugieSlowo = input("drugie słowo: ")
    wysokosc = len(pierwszeSlowo) + 1
    szerokosc = len(drugieSlowo) + 1
    macierz = [[0 for n in range(szerokosc)] for m in range(wysokosc)]

    for i in range(wysokosc):
        macierz[i][0] = i
    for j in range(szerokosc):
        macierz[0][j] = j

    for i in range(1, wysokosc):
        for j in range(1, szerokosc):

            if pierwszeSlowo[i - 1] == drugieSlowo[j - 1]:
                koszt = 0   # dla takich samych znaków
            else:
                koszt = 1   # dla różnych znaków

            macierz[i][j] = min(
                macierz[i - 1][j] + 1,        # komórka do góry, usunięcie
                macierz[i][j - 1] + 1,        # komórka z lewej, wstawienie
                macierz[i - 1][j - 1] + koszt # komórka po skosie, zamiana
            )
    wyswietlMacierz(macierz)




levenshtein()