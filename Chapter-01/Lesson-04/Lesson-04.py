# Lesson 4: Understanding Class and Instance Attributes
# Concept: The Difference Between Class Attributes and Instance Attributes
# By \ Fayez Moawad

class Car:
    # Class attribute
    wheels = 4  # All cars have 4 wheels by default

    def __init__(self, brand, color, year):
        # Instance attributes
        self.brand = brand
        self.color = color
        self.year = year
    
    def display_info(self):
        print(f"This {self.color} {self.brand} from {self.year} has {Car.wheels} wheels.")

# Creating two objects
car1 = Car("Toyota", "Red", 2020)
car2 = Car("Honda", "Blue", 2021)

# Displaying information
car1.display_info()  # Output: This Red Toyota from 2020 has 4 wheels.
car2.display_info()  # Output: This Blue Honda from 2021 has 4 wheels.

# Instance Attributes can be modified directly on the object
car1.color = "Green"
print(car1.color)  # Output: Green

# Class Attributes can be modified directly using the class name or any instance
# affects all instances
Car.wheels = 6
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6


# Class Attribute wheels: Defined at the class level, so it’s shared among all instances. 
# Changing Car.wheels affects all instances.
# Instance Attributes brand, color, year: Defined in __init__, unique to each object.