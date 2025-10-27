# Funkcja jako obiekt
def przywitaj():
    print("Cześć!")

x = przywitaj
x()
print(type(x))

"""
Funkcje wyższego rzędu
Funkcja wyższego rzędu to taka, która przyjmuje inne funkcje jako argumenty lub zwraca funkcję. Np.:

map(func, iterable) -> stosuje funkcję na każdym elemencie ob. iterowalnego
filter(func, iterable) -> filtruje elementy przez funkcję (zwraca tylko prawdziwe)
sorted(iterable, key=func) -> sortuje (też wspak)
functools.reduce(func, iterable) -> podobna do map, wykonuje na wszystkich elementach po 2 (((1+2)+3)+4)
Funkcje wewnętrzne i domknięcia
"""
def witaj(imie):
    def komunikat():
        return f"Cześć, {imie}!"
    return komunikat

p = witaj("Anna")
print(p())  # -> Cześć, Anna!

# Dekorator
# Dekorator to funkcja, która przyjmuje inną funkcję i zwraca nową funkcję wzbogaconą o dodatkowe działanie.

# równoważne hello = dekorator(hello)

def dekorator(func):
    def wrapper():
        print("Zanim wywołam funkcję...")
        func()
        print("...a to po niej.")
    return wrapper

@dekorator
def hello():
    print("Hello, world!")

hello()

# ----------------------------------------

def powiel(ile_razy):
   def dekorator(func):
      def wrapper(*args, **kwargs):
         for _ in range(ile_razy):
            func(*args, **kwargs)
      return wrapper
   return dekorator

@powiel(3)
def hello():
    print("Hej!")

hello()

# (dekorator z argumentami -> 3 poziomy)

# ----------------------------------------

# @measure_time
# @logger
# def test():
#     time.sleep(1)

# (od dołu do góry)

