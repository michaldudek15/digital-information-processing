"""
Projekt to symulacja wypożyczalni pojazdów.
System ma przechowywać listę dostępnych pojazdów (samochody, rowery, ciężarówki), umożliwiać ich wypożyczanie, zwracanie, oraz generować raporty o stanie floty.

Vehicle (klasa bazowa), truck, bike, car.
Każdy pojazd ma wspólne pola (id, name, busy) i metody (__str__, rent(), return_()).

System wypożyczalni (klasa Rental) zarządza listą pojazdów — czyli kompozycja.

Logger (Singleton), każde wypożyczenie i zwrot może być logowane do pliku.

Użycie:

rental = Rental([Car(1, "Mazda"), Bike(2, "Trek"), Truck(3, "Volvo")])
rental.list_all()
rental.rent(1)
rental.rent(2)
rental.return_(1)

self.logger = Logger()
self.logger.log(f"Wypożyczono pojazd {v.name}")
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.busy = False

    @abstractmethod
    def __str__(self):
        pass

    def rent(self):
        self.busy = True

    def return_(self):
        self.busy = False

class Car(Vehicle):
    def __str__(self):
        status = "wypożyczony" if self.busy else "dostępny"
        return f"Samochód {self.name} (ID: {self.id}) - {status}"

class Bike(Vehicle):
    def __str__(self):
        status = "wypożyczony" if self.busy else "dostępny"
        return f"Rower {self.name} (ID: {self.id}) - {status}"

class Truck(Vehicle):
    def __str__(self):
        status = "wypożyczony" if self.busy else "dostępny"
        return f"Ciężarówka {self.name} (ID: {self.id}) - {status}"
    
class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename="rental_log.txt"):
        if hasattr(self, 'initialized'):
            return  
        if not hasattr(self, 'initialized'):
            self.filename = filename
            self.initialized = True

    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')

class Rental:
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.logger = Logger()

    def list_all(self):
        for v in self.vehicles:
            print(v)

    def rent(self, vehicle_id):
        for v in self.vehicles:
            if v.id == vehicle_id and not v.busy:
                v.rent()
                self.logger.log(f"Wypożyczono pojazd {v.name}")
                return f"Wypożyczono pojazd {v.name}"
        return "Pojazd niedostępny lub nie istnieje."

    def return_(self, vehicle_id):
        for v in self.vehicles:
            if v.id == vehicle_id and v.busy:
                v.return_()
                self.logger.log(f"Zwrócono pojazd {v.name}")
                return f"Zwrócono pojazd {v.name}" 
        return "Pojazd nie był wypożyczony lub nie istnieje."
    
rental = Rental([Car(1, "Mazda"), Bike(2, "Trek"), Truck(3, "Volvo")])
rental.list_all()
print(rental.rent(1))
print(rental.rent(2))
print(rental.return_(1))
rental.list_all()