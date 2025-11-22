import csv
import json

def json2csv(json_file, csv_file):
    with open(json_file, encoding="utf-8") as f:
        dane = json.load(f)

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = None

        for element in dane:
            if writer is None:
                writer = csv.DictWriter(f, fieldnames=element.keys())
                writer.writeheader()

            writer.writerow(element)