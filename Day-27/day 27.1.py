print("2. ABSTRACTION - VEHICLE")
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def fuel_type(self):
        print("This vehicle uses fuel.")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key.")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with kick.")
c = Car()
c.start_engine()
c.fuel_type()
b = Bike()
b.start_engine()

