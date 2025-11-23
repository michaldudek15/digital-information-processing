import re
from collections import Counter

def wczytaj_tekst(plik):
    with open(plik, "r") as plik:
        tekst = plik.read().lower()
        return re.sub(r"[^a-ząćęłńóśżźà ]", "", tekst)
        
def ngramy(tekst, n):
    return [tekst[i:i+n] for i in range(len(tekst)-n+1)]

def policz_ngramy(tekst, n):
    return dict(Counter(ngramy(tekst, n)))

def ranking(ngram_dict):
    return sorted(ngram_dict.items(), key=lambda x: x[1], reverse=True)


tekst = wczytaj_tekst("KORPUSY/POL/POL1 Pan Tadeusz.txt")

unigramy = policz_ngramy(tekst, 1)
digramy  = policz_ngramy(tekst, 2)
trigramy = policz_ngramy(tekst, 3)

ranking_unigramow = ranking(unigramy)
ranking_digramow = ranking(digramy)
ranking_trigramow = ranking(trigramy)

# Wyświetlenie TOP 20
print("20 najczęstszych unigramów:")
for gram, count in ranking_unigramow[:20]:
    print(gram, count)

print("\n20 najczęstszych digramów:")
for gram, count in ranking_digramow[:20]:
    print(gram, count)

print("\n20 najczęstszych trigramów:")
for gram, count in ranking_trigramow[:20]:
    print(gram, count)


print("UNIGRAMY:\n", unigramy)
print("\nDIGRAMY:\n", digramy)
print("\nTRIGRAMY:\n", trigramy)
    