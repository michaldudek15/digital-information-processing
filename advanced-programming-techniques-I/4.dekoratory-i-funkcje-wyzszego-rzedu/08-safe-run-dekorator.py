"""
Proszę przygotować dekorator @safe_run, który przechwytuje błędy występujące w udekorowanej funkcji 
i zamiast przerywać program, wypisuje komunikat o błędzie w przyjaznej formie.

- przyjmuje funkcję jako argument,
- uruchamia ją w bloku try/except,
- w przypadku wystąpienia błędu wypisuje komunikat `[Błąd] <typ błędu>: <treść błędu>`
- zwraca `None` zamiast błędu.


@safe_run
def dzielenie(a, b):
    return a / b

print(dzielenie(10, 2))   # poprawne
print(dzielenie(10, 0))   # dzielenie przez zero
"""

def safe_run(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[Błąd] {type(e).__name__}: {e}")
            return None
    return wrapper

@safe_run
def dzielenie(a, b):
    return a / b    

print(dzielenie(10, 2))   # poprawne
print(dzielenie(10, 0))   # dzielenie przez zero

