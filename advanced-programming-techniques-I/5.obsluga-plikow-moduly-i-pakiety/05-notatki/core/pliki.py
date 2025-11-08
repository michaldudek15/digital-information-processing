import json
from pathlib import Path

SCIEZKA_PLIKU = Path(__file__).parent.parent / "data" / "notatki.json"

def wczytaj_notatki():
    if not SCIEZKA_PLIKU.exists():
        return []
    with open(SCIEZKA_PLIKU, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def zapisz_notatki(notatki):
    with open(SCIEZKA_PLIKU, "w", encoding="utf-8") as f:
        json.dump(notatki, f, indent=4, ensure_ascii=False)