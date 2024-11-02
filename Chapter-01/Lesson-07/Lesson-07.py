# Lesson 7: Inheritance in Python OOP
# Concept: Understanding Inheritance and How to Use It. By \ Fayez Moawad


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"This is a {self.brand} from {self.year}.")

# Inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, year, color):
        # Call the parent class's constructor
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        # Extend the parent method
        super().display_info()
        print(f"It is {self.color} in color.")

# Creating objects
my_vehicle = Vehicle("Generic Brand", 2015)
my_vehicle.display_info()  # Output: This is a Generic Brand from 2015.

my_car = Car("Toyota", 2020, "Red")
my_car.display_info()  
# Output:
# This is a Toyota from 2020.
# It is Red in color.



# Vehicle Class: The parent class that has attributes brand and year and a method display_info().
# Car Class: The child class that inherits from Vehicle and adds an additional attribute color.
# super(): Used in Car.__init__() to call the __init__() method of Vehicle to initialize brand 
# and year. Also used in display_info() to extend the functionality of the parent method.