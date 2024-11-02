# Lesson 1: Introduction to Object-Oriented Programming
# Concept: Understanding the Basics of OOP by \ Fayez Moawad

class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Attribute
        self.color = color  # Attribute
    
    def start_engine(self):  # Method
        print("The engine is starting...")

# Creating an object from the class
my_car = Car("Toyota", "Red")

# Accessing attributes and methods
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red
my_car.start_engine()  # Output: The engine is starting...



# The class Car: defines a template.
# __init__ is a special method called a initializer that initializes an object’s attributes.
# self refers to the instance itself.
# We create an object my_car using Car("Toyota", "Red").
# We access its attributes using my_car.brand and my_car.color.
# We call the method my_car.start_engine().
