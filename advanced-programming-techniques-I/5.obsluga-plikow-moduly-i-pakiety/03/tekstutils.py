"""
Proszę utworzyć moduł `tekstutils.py` z funkcjami:
- policz_slowa(napis) – zwraca liczbę słów w napisie,
- odwroc(napis) – zwraca odwrócony napis.

Proszę następnie zaimportować moduł w pliku `main.py` 
i przetestować jego działanie.
"""

def policz_slowa(napis):
    """Zwraca liczbę słów w napisie."""
    return len(napis.split())

def odwroc(napis):
    """Zwraca odwrócony napis."""
    return napis[::-1]
