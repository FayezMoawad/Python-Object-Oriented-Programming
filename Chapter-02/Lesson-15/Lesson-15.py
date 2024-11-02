# Lesson 15: Implementing Interfaces with Python OOP
# Concept: Understanding and Using Interfaces in Python by \ Fayez Moawad

from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

# Implementing the interface in the Car class
class Car(IVehicle):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"{self.brand} engine started.")

    def stop_engine(self):
        print(f"{self.brand} engine stopped.")

    def display_info(self):
        print(f"This is a {self.brand} car from {self.year}.")

# Implementing the interface in another class
class Truck(IVehicle):
    def __init__(self, brand, year, load_capacity):
        self.brand = brand
        self.year = year
        self.load_capacity = load_capacity

    def start_engine(self):
        print(f"{self.brand} truck engine started.")

    def stop_engine(self):
        print(f"{self.brand} truck engine stopped.")

    def display_info(self):
        print(f"This is a {self.brand} truck from {self.year} with a load capacity of {self.load_capacity} tons.")

# Creating objects
car = Car("Toyota", 2020)
truck = Truck("Volvo", 2018, 15)

# Using the methods
car.start_engine()  # Output: Toyota engine started.
car.display_info()  # Output: This is a Toyota car from 2020.
truck.display_info()  # Output: This is a Volvo truck from 2018 with a load capacity of 15 tons.


# IVehicle Class: Serves as an interface with abstract methods (start_engine(), stop_engine(), 
# display_info()).
# Car and Truck Classes: Implement the interface by providing their own versions of the methods 
# defined in IVehicle.
# Abstract methods in IVehicle ensure that any subclass implements these methods, 
# creating a consistent structure across related classes.
