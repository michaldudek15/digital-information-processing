"""
Proszę utworzyć plik `konfiguracja.json` o przykładowej zawartości:

```
{
  "język": "pl",
  "motyw": "ciemny",
  "liczba_użytkowników": 4
}
```

Program ma wczytać plik i wyświetlić wszystkie klucze i wartości w czytelnej formie.
"""

import json

with open("konfiguracja.json", "r") as plik:
    dane = json.load(plik)

for klucz, wartosc in dane.items():
    print(f"{klucz}: {wartosc}")
    


