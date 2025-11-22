import csv
import json

def csv2json(csv_file, json_file):
    dane = []

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for wiersz in reader:
            dane.append(wiersz)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dane, f, indent=4, ensure_ascii=False)