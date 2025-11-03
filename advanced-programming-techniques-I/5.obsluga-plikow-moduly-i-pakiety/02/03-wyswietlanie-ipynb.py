"""
Proszę napisać program, który:
- wyświetli wszystkie pliki .ipynb w bieżącym katalogu,
- dla każdego pliku poda jego rozmiar w bajtach.

Proszę użyć modułu pathlib.
"""

from pathlib import Path

sciezka = Path(".").glob("*.ipynb")

for plik in sciezka:
    print(f"Plik: {plik.name}, Rozmiar: {plik.stat().st_size} bajtów") 

