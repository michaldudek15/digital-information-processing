"""
Proszę utworzyć dwa dekoratory:
- `@uppercase` – zamieniający zwracany tekst na wielkie litery,
- `@exclaim` – dodający na końcu wykrzyknik.

@exclaim
@uppercase
def greet(name):
    return f"Hello {name}"

Proszę sprawdzić kolejność działania dekoratorów, a następnie zamienić ich kolejność i porównać wynik.
"""

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!aaa"
    return wrapper

@exclaim   # wykonuje się jako drugi
@uppercase # wykonuje się jako pierwszy
def powitaj(name):
    return "elo" + name

print(powitaj(" Michał"))