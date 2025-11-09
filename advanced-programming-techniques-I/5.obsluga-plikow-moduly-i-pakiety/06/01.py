"""
Przetworzyć plik `/var/log/apache2/access.log`, wyciągnąć z niego istotne informacje statystyczne i zapisać raport do pliku CSV lub JSON.

- liczbę wszystkich żądań,
- liczbę unikalnych adresów IP,
- najczęściej odwiedzane zasoby (/index.html, /login, /img/logo.png itp.),
- rozkład kodów odpowiedzi HTTP (np. 200, 404, 500).

Program na koniec zapisze wyniki do pliku `raport.json` w formacie:

```
{
  "liczba_żądań": 2457,
  "unikalne_ip": 57,
  "top_zasoby": {
    "/": 432,
    "/login": 128,
    "/favicon.ico": 97
  },
  "kody_http": {
    "200": 2134,
    "404": 185,
    "500": 6
  }
}
```

Dodatkowo wyświetli 5 najczęściej odwiedzających adresów IP.
"""

import re
import json
from collections import Counter

output_path = "raport.json"

log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+)(?: \S+)?" (?P<status>\d{3}) (?P<size>\S+)'
)

liczba_zadan = 0
ip_counter = Counter()
zasoby_counter = Counter()
status_counter = Counter()

with open("access.log", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        match = log_pattern.search(line)
        if not match:
            continue
        liczba_zadan += 1

        ip = match.group("ip")
        path = match.group("path")
        status = match.group("status")

        ip_counter[ip] += 1
        zasoby_counter[path] += 1
        status_counter[status] += 1

raport = {
    "liczba_żądań": liczba_zadan,
    "unikalne_ip": len(ip_counter),
    "top_zasoby": dict(zasoby_counter.most_common(3)),
    "kody_http": dict(status_counter),
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(raport, f, ensure_ascii=False, indent=2)

print("najczęstsze adresy IP:")
for ip, count in ip_counter.most_common(5):
    print(f"{ip}: {count}")

print(f"\nraport zapisano do pliku: {output_path}")