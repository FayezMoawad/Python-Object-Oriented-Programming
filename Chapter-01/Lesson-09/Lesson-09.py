# Lesson 9: Abstraction in Python OOP
# Concept: Understanding and Implementing Abstraction
# By \ Fayez Moawad


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def display_info(self):
        pass  # Abstract method, no implementation

# Subclass that implements the abstract method
class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        print(f"This car is a {self.color} {self.brand} from {self.year}.")

class Truck(Vehicle):
    def __init__(self, brand, year, load_capacity):
        super().__init__(brand, year)
        self.load_capacity = load_capacity

    def display_info(self):
        print(f"This truck is a {self.brand} from {self.year} with a load capacity of {self.load_capacity} tons.")

# Creating objects
my_car = Car("Toyota", 2020, "Red")
my_truck = Truck("Volvo", 2018, 15)

# Calling the method
my_car.display_info()  # Output: This car is a Red Toyota from 2020.
my_truck.display_info()  # Output: This truck is a Volvo from 2018 with a load capacity of 15 tons.

# Attempting to create an object of the abstract class (will raise an error)
# my_vehicle = Vehicle("Generic", 2022)  # Uncommenting this line raises TypeError



# Abstract Class (Vehicle): Acts as a blueprint and cannot be instantiated. 
# It contains an @abstractmethod that must be implemented by any subclass.
# Concrete Subclasses (Car, Truck): These classes inherit from Vehicle and provide 
# their own implementation of the display_info() method.
# ABC Module: Ensures that Vehicle cannot be instantiated directly, 
# and display_info() must be implemented in any subclass.