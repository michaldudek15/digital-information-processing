"""Proszę stworzyć abstrakcyjną klasę Transport z metodą cost(distance).
Następnie klasy Car, Train, Plane i porównać koszty pokonania 250 km.
"""

from abc import ABC, abstractmethod 

class Transport(ABC):
    @abstractmethod
    def cost(self, distance):
        pass

class Car(Transport):
    def cost(self, distance):
        return distance * 0.5

class Train(Transport):
    def cost(self, distance):
        return distance * 0.3

class Plane(Transport):
    def cost(self, distance):
        return distance * 1.2

distance = 250
car = Car()
train = Train()
plane = Plane()

print(f"koszt podróży 250 km samochodem: {car.cost(distance)}")
print(f"koszt podróży 250 km pociągiem: {train.cost(distance)}")
print(f"koszt podróży 250 km samolotem: {plane.cost(distance)}")