"""
Proszę utworzyć moduł `tekstutils.py` z funkcjami:
- policz_slowa(napis) – zwraca liczbę słów w napisie,
- odwroc(napis) – zwraca odwrócony napis.

Proszę następnie zaimportować moduł w pliku `main.py` 
i przetestować jego działanie.
"""

from tekstutils import policz_slowa, odwroc

napis = "Ala ma kota"
print(f"Liczba słów w napisie: {policz_slowa(napis)}")
print(f"Odwrócony napis: {odwroc(napis)}")
