# Lesson 10: Composition in Python OOP
# Concept: Understanding Composition and How It Differs from Inheritance
# By \ Fayez Moawad

class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

    def start(self):
        print(f"The {self.type} engine with {self.horsepower} HP is starting...")

class Car:
    def __init__(self, brand, year, engine):
        self.brand = brand
        self.year = year
        self.engine = engine  # Composition: Car "has an" Engine

    def display_info(self):
        print(f"This is a {self.brand} from {self.year} with an engine specification:")
        self.engine.start()  # Using the Engine's method

# Creating an Engine object
my_engine = Engine(300, "V6")

# Creating a Car object that includes the Engine object
my_car = Car("Toyota", 2020, my_engine)

# Displaying car information
my_car.display_info()
# Output:
# This is a Toyota from 2020 with an engine specification:
# The V6 engine with 300 HP is starting...


# Engine Class: Represents an engine with attributes horsepower and type and a method start().
# Car Class: Uses composition by including an Engine instance as an attribute.
# When my_car.display_info() is called, it also calls the start() method of the Engine instance, 
# demonstrating how composition allows for more complex behavior.