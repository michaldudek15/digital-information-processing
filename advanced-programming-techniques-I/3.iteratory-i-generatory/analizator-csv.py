"""
Proszę napisać prosty analizator CSV, który:

otwiera plik np. sales.csv,
czyta go liniowo (bez wczytywania całości),
zwraca tylko rekordy, gdzie wartość sprzedaży > 1000,
oblicza średnią wartość sprzedaży tych rekordów.
sales = (x for x in read_sales("sales.csv") if x > 1000)
avg = sum(sales) / len(list(sales))  # uwaga! list() zużywa generator
"""
import csv

def read_sales(path):
        with open(path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    quantity = int(row["quantity"])
                    price = float(row["price"])
                    sales_value = quantity * price
                    if sales_value > 1000:
                        yield sales_value
                except (ValueError, KeyError):
                    continue


high_sales = [x for x in read_sales("sales.csv")]

if high_sales:
    avg = sum(high_sales) / len(high_sales)
    print("średnia wartość sprzedaży powyżej 1000: ", avg)
else:
    print("nie ma sprzedaży powyżej 1000") 

