# Lesson 8: Polymorphism in Python OOP
# Concept: Understanding Polymorphism and How to Implement It
# By \ Fayez Moawad


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"This is a {self.brand} from {self.year}.")

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

# Polymorphic behavior
vehicles = [Car("Toyota", 2020, "Red"), Truck("Volvo", 2018, 15), Vehicle("Generic Brand", 2015)]

for vehicle in vehicles:
    vehicle.display_info()


# display_info() Method: Each class (Car, Truck, Vehicle) has its own implementation 
# of display_info().
# Polymorphism: The for loop calls display_info() on different objects, but the correct 
# method is invoked for each class. This allows the same code to work with different 
# types of vehicles without modification.