class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def info(self):
        return f"{self.name}, rok {self.year}"

s = Student("Anna", 2)
print(s.info())

# Dziedziczenie – klasy pochodne rozszerzają bazową.
# Polimorfizm – różne obiekty mają wspólne API (te same nazwy metod).

class Animal:
    def speak(self):
        return "?"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

for a in [Dog(), Cat()]:
    print(a.speak())

#######################################################################

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Cześć, jestem {self.name}")

class Worker(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
    def greet(self):
        super().greet()
        print(f"Pracuję jako {self.job}.")

# Klasowa (@classmethod) – pracuje na cls, ma dostęp do zmiennych klasy ale nie do instancji
# Statyczna – nie używa self i cls, pomocnicza (zwykłe funkcje, ale umieszczone w klasie dla porządku / logicznego pogrupowania)

class Student:
    school = "UJ"
    
    @classmethod
    def get_school(cls):
        return cls.school

print(Student.get_school())   # UJ

#Alternatywny konstruktor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)

p = Person.from_birth_year("Adam", 1990)


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(2, 3))   # 5

# Klasa abstrakcyjna – nie może być instancjonowana. Służy jako szablon dla innych klas. W Pythonie klasa abstrakcyjna = interfejs + możliwość częściowej implementacji.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(Payment):
    def pay(self, amount):
        print(f"Płacę {amount} zł przez PayPal")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Płacę {amount} zł kartą")

class BadClass(Payment):
    pass

# kompozycja – obiekt zawiera inny obiekt, zarządza nim

# agregacja – obiekt tylko korzysta z zewnętrznego obiektu

class Engine:
    def start(self): print("Silnik uruchomiony")

class Car:
    def __init__(self):
        self.engine = Engine()  # kompozycja
    def drive(self):
        self.engine.start()
        print("Samochód jedzie")

##############################################################

class Author:
    def __init__(self, name): self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title; self.author = author

# Singleton – tylko jedna instancja

class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory – fabryka obiektów

class TransportFactory:
    @staticmethod
    def create(kind):
        if kind == "car": return Car()
        if kind == "plane": return Plane()

# Strategy – wymienialne zachowania

class Payment:
    def pay(self, amount): pass

class PayPal(Payment):
    def pay(self, amount): print("PayPal:", amount)

class CreditCard(Payment):
    def pay(self, amount): print("Card:", amount)

class Order:
    def __init__(self, strategy):
        self.strategy = strategy
    def checkout(self, amount):
        self.strategy.pay(amount)

order1 = Order(PayPal())
order1.checkout(100)

