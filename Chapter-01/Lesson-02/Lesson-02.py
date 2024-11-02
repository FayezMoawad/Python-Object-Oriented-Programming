# Lesson 2: Understanding __init__ and self
# Concept: The Constructor Method __init__ and the Use of self by \ Fayez Moawad

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand  # Instance attribute
        self.color = color  # Instance attribute
        self.year = year    # Instance attribute
    
    def display_info(self):
        print(f"This car is a {self.color} {self.brand} from {self.year}.")

# Creating an object with more attributes
my_car = Car("Toyota", "Red", 2020)

# Using the display_info method to print details about the car
my_car.display_info()  # Output: This car is a Red Toyota from 2020.



# __init__ takes brand, color, and year as parameters and assigns them to self.brand,
# self.color, and self.year, making them attributes of the object.
# The display_info() method prints the attributes using self to reference them.
# When we create my_car, __init__ runs automatically, setting brand, color, and year as
# properties of my_car.
# Why self Is Important:
# It differentiates between instance attributes and local variables.
# Without self, the attributes would not belong to the object itself, making them inaccessible
# outside of the constructor or class methods.