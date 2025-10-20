import csv
import pandas as pd

# wczytanie danych z pliku CSV
try:
    with open("oceny.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dane = list(reader)
        print(f"Wczytano {len(dane)} rekordów.")
except FileNotFoundError:
        print("Błąd: nie znaleziono pliku z danymi.")
except Exception as e:
        print("Nieoczekiwany błąd podczas wczytywania danych:", e)

# lista przedmiotów
przedmioty = ["matematyka", "python", "angielski", "algorytmy", "bazy_danych", "ai"]

for rekord in dane:
    # konwersja ocen na int, "nzal" pozostaje jako string
    for przedmiot in przedmioty:
        if rekord[przedmiot] != "nzal":
            rekord[przedmiot] = int(rekord[przedmiot])
        else:
            pass

    # obliczenie średniej i wypisanie wyników (suma ocen innych od nzal podzielona przez liczbę wszystkich przedmiotów)
    rekord["srednia"] = sum([rekord[przedmiot] for przedmiot in przedmioty if isinstance(rekord[przedmiot], int)]) / len(przedmioty)
    
    # dodanie liczby przedmiotów, które zaliczył student
    rekord["liczba_zaliczonych_przedmiotów"] = sum(isinstance(rekord[przedmiot], int) for przedmiot in przedmioty)


# wypisanie wyników w formie tabeli
df = pd.DataFrame(dane)
print(df)

# posortowanie studentów według średniej i wypisanie rankingu
ranking = sorted(dane, key=lambda rekord: rekord["srednia"], reverse=True)
df_ranking = pd.DataFrame(ranking)
print(df_ranking)

# lista studentów bez żadnego "nzal"
studenci_bez_nzal = [rekord for rekord in dane
    if all(isinstance(rekord[przedmiot], int) for przedmiot in przedmioty)
    ]

# wypisanie studentów bez żadnego "nzal"
print("studenci bez żadnego 'nzal':")
for rekord in studenci_bez_nzal:
    print(f"{rekord['imie']} {rekord['nazwisko']}")

# obliczenie średniej ocen w grupie A
studenci_A = [rekord for rekord in dane if rekord["grupa"] == "A"]
ocenyA = []

for rekord in studenci_A:
    ocenyA.extend([rekord[przedmiot] for przedmiot in przedmioty if isinstance(rekord[przedmiot], int)])

sredniaA = sum(ocenyA) / len(ocenyA) if ocenyA else 0
print(f"średnia ocen grupy A: {sredniaA:.2f}")

# obliczenie średniej ocen w grupie B
studenci_B = [rekord for rekord in dane if rekord["grupa"] == "B"]
ocenyB = []

for rekord in studenci_B:
    ocenyB.extend([rekord[przedmiot] for przedmiot in przedmioty if isinstance(rekord[przedmiot], int)])

sredniaB = sum(ocenyB) / len(ocenyB) if ocenyB else 0
print(f"średnia ocen grupy B: {sredniaB:.2f}")

# porównanie średnich grup A i B
if sredniaA > sredniaB:
    print("grupa A ma wyższą średnią ocen.")
elif sredniaB > sredniaA:
    print("grupa B ma wyższą średnią ocen.")
else:
    print("obie grupy mają taką samą średnią ocen")



# zliczenie liczby studentów z "nzal" w każdej grupie
liczba_nzal_A = sum(1 for rekord in studenci_A if any(rekord[przedmiot] == "nzal" for przedmiot in przedmioty))
liczba_nzal_B = sum(1 for rekord in studenci_B if any(rekord[przedmiot] == "nzal" for przedmiot in przedmioty))

# wypisanie procenta studentów z "nzal" w każdej grupie
print(f"liczba studentów z 'nzal' w grupie A: {liczba_nzal_A/len(studenci_A) * 100}%")
print(f"liczba studentów z 'nzal' w grupie B: {liczba_nzal_B/len(studenci_B) * 100}%")

# obliczenie średniej oceny dla każdego przedmiotu
srednie_z_przedmiotow = {}
for przedmiot in przedmioty:
    oceny = [rekord[przedmiot] for rekord in dane if isinstance(rekord[przedmiot], int)]
    srednia = sum(oceny) / len(oceny) if oceny else 0
    srednie_z_przedmiotow[przedmiot] = srednia

# wyświetlenie wyników
print("średnie ocen dla każdego przedmiotu:")
for przedmiot, srednia in srednie_z_przedmiotow.items():
    print(f"{przedmiot}: {srednia:.2f}")

# zliczenie liczby ocen 5 dla każdego przedmiotu
oceny_5 = {}
for przedmiot in przedmioty:
    oceny_5[przedmiot] = sum(1 for rekord in dane if rekord[przedmiot] == 5)

# znalezienie przedmiotu z największą liczbą 5
najwiecej_5_przedmiot = max(oceny_5, key=oceny_5.get)
print(f"przedmiot najczęściej oceniany na 5: {najwiecej_5_przedmiot} ({oceny_5[najwiecej_5_przedmiot]} razy)")

# zliczenie liczby "nzal" dla każdego przedmiotu
oceny_nzal = {}
for przedmiot in przedmioty:
    oceny_nzal[przedmiot] = sum(1 for rekord in dane if rekord[przedmiot] == "nzal")

# znalezienie przedmiotu z największą liczbą "nzal"
przedmiot_najwiecej_nzal = max(oceny_nzal, key=oceny_nzal.get)
print(f"przedmiot z największą liczbą 'nzal': {przedmiot_najwiecej_nzal} ({oceny_nzal[przedmiot_najwiecej_nzal]} razy)")

# zapisanie wyników studentów do pliku csv
with open("wyniki_studenci.csv", "w", newline="", encoding="utf-8") as f:
    naglowki = ["imie", "nazwisko", "grupa"] + przedmioty + ["srednia", "liczba_zaliczonych_przedmiotów"]
    writer = csv.DictWriter(f, fieldnames=naglowki)
    writer.writeheader()
    for rekord in dane:
        writer.writerow(rekord)

# zapisanie rankingu studentów do pliku csv
with open("ranking_studenci.csv", "w", newline="", encoding="utf-8") as f:
    naglowki = ["imie", "nazwisko", "grupa"] + przedmioty + ["srednia", "liczba_zaliczonych_przedmiotów"]
    writer = csv.DictWriter(f, fieldnames=naglowki)
    writer.writeheader()
    for rekord in ranking:
        writer.writerow(rekord)

# zapisanie porównania grup do pliku csv
with open("srednie_grupy.csv", "w", newline="", encoding="utf-8") as f:
    naglowki = ["grupa", "srednia", "procent_studentow_z_nzal"]
    writer = csv.DictWriter(f, fieldnames=naglowki)
    writer.writeheader()
    writer.writerow({"grupa": "A", "srednia": round(sredniaA, 2), "procent_studentow_z_nzal": liczba_nzal_A / len(studenci_A) * 100})
    writer.writerow({"grupa": "B", "srednia": round(sredniaB, 2), "procent_studentow_z_nzal": liczba_nzal_B / len(studenci_B) * 100})

print("\nCZYTELNY RAPORT KONSOLOWY\n")

# 5 najlepszych studentów według średniej
print("studenci z najlepszą średnią:")
top5 = ranking[:5]
for i in range(len(top5)):
    rekord = top5[i]
    print(str(i+1) + ". " + rekord['imie'] + " " + rekord['nazwisko'] + " - średnia: " + str(round(rekord['srednia'],2)))

# średnie ocen dla każdej grupy
print("\nśrednie ocen dla grup:")
print(f"grupa A: {sredniaA:.2f}")
print(f"grupa B: {sredniaB:.2f}")

najlatwiejszy = max(srednie_z_przedmiotow, key=srednie_z_przedmiotow.get)
najtrudniejszy = min(srednie_z_przedmiotow, key=srednie_z_przedmiotow.get)
print(f"najłatwiejszy przedmiot (z najwyższą średnią): {najlatwiejszy} ({srednie_z_przedmiotow[najlatwiejszy]})")
print(f"najtrudniejszy przedmiot (z najniższą średnią): {najtrudniejszy} ({srednie_z_przedmiotow[najtrudniejszy]})")