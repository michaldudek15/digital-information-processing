"""
Proszę przygotować mały projekt w strukturze:
```
notatki/
│
├── data/
│   └── notatki.json
│
├── core/
│   ├── __init__.py
│   ├── pliki.py
│   └── notatnik.py
│
└── main.py
```

Wymagania:

- pliki.py – funkcje do zapisu/odczytu JSON,
- notatnik.py – funkcje dodawania, wyszukiwania i usuwania
 notatek,
- main.py – prosty interfejs tekstowy (menu),
po uruchomieniu użytkownik może dodawać i przeglądać notatki.
"""

from core.notatnik import dodaj_notatke, wyszukaj_notatke, usun_notatke, pokaz_wszystkie


def menu():
    while True:
        print("\n1. dodaj notatkę")
        print("2. wyświetl wszystkie notatki")
        print("3. wyszukaj notatkę")
        print("4. usuń notatkę")
        print("5. wyjdź z programu")

        wybor = input("wybierz opcję: ")

        if wybor == "1":
            tytul = input("tytuł notatki: ")
            tresc = input("treść notatki: ")
            dodaj_notatke(tytul, tresc)
            print("notatka została dodana")
        elif wybor == "2":
            notatki = pokaz_wszystkie()
            if not notatki:
                print("brak notatek")
            else:
                for n in notatki:
                    print(f"\n📘 {n['tytul']}\n{n['tresc']}")
        elif wybor == "3":
            slowo = input("podaj słowo kluczowe do wyszukania: ")
            wyniki = wyszukaj_notatke(slowo)
            if not wyniki:
                print("brak wyników")
            else:
                for n in wyniki:
                    print(f"\n📗 {n['tytul']}\n{n['tresc']}")
        elif wybor == "4":
            tytul = input("podaj tytuł notatki do usunięcia: ")
            if usun_notatke(tytul):
                print("notatka została usunięta")
            else:
                print("nie znaleziono notatki o takim tytule")
        elif wybor == "5":
            break
        else:
            print("niepoprawny wybór, spróbuj ponownie")


if __name__ == "__main__":
    menu()