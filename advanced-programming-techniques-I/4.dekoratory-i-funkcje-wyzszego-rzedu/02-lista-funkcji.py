"""
Proszę utworzyć listę trzech wbudowanych funkcji, np. lista = [len, sum, max].
Proszę wypisać nazwę każdej funkcji (korzystając z atrybutu __name__.) oraz jej wynik

lista_funkcji = [len, sum, max]
lista_argumentow = list(range(10))
naszaf(lista_funkcji, list_argumentow)

wynik działania:
    'len', 5
    'sum', 15
    'max', 5
"""
lista = list(range(5))

print(lista)

lista_funkcji = [len, sum, max]
lista_argumentow = lista

def naszaf(lista_funkcji, lista_argumentow):
    for funkcja in lista_funkcji:
        wynik = funkcja(lista_argumentow)
        print(f"'{funkcja.__name__}', {wynik}")
        
naszaf(lista_funkcji, lista_argumentow)
