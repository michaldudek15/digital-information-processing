"""
Proszę stworzyć pakiet `konwersja`, zawierający:

- csv2json.py – funkcję konwertującą CSV → JSON,
- json2csv.py – funkcję konwertującą JSON → CSV,

```from konwersja import csv2json, json2csv```

Program testowy ma przekształcić plik produkty.csv w produkty.json i odwrotnie.
"""

from konwersja import csv2json, json2csv

csv2json("przyklad1.csv", "produkty.json")
json2csv("przyklad2.json", "produkty.csv")

print("konwersja zakończona")