"""
Proszę stworzyć moduł z funkcją `zapisz_log(typ, wiadomosc)`, która:

zapisze dane do pliku app.log w formacie:
```
[2025-11-02 18:35:22] [INFO] Program uruchomiony
```

TIP: wykorzysta moduł datetime.
 
Proszę następnie zaimportować moduł w innym skrypcie i zarejestrować kilka wpisów.
"""


from logger import zapisz_log

zapisz_log("info", "log informaccyjny")
zapisz_log("warning", "ostrzeżenie przed niebezpieczeństwem")
zapisz_log("error", "error404")
zapisz_log("debug", "szczegóły działania funkcji")