"""
zapisuje dane do pliku app.log w formacie:
[2025-11-02 18:35:22] [INFO] Program uruchomiony
"""

import datetime

def zapisz_log(typ, wiadomosc):
    czas = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a", encoding="utf-8") as file:
        file.write(f"[{czas}] [{typ.upper()}] {wiadomosc}\n")