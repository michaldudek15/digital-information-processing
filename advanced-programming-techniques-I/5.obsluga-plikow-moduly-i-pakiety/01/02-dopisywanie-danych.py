"""
Proszę utworzyć program, który poprosi użytkownika o imię i wiek, a następnie zapisze te dane do pliku `dane.txt` w formacie:

```
Imię: Anna, Wiek: 23
```

Jeśli plik już istnieje, proszę dopisać dane na końcu.
"""
filename = "dane.txt"

imie = input(f"Podaj imię do pliku {filename}: ")
wiek = input(f"Podaj wiek do pliku {filename}: ")

with open(filename, "a") as plik:
    plik.write(f"Imię: {imie}, Wiek: {wiek}\n")
print(f"Dane zostały zapisane do pliku {filename}")
