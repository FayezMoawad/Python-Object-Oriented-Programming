# Lesson 5: Encapsulation and Access Modifiers
# Concept: What is Encapsulation and How to Use Access Modifiers
# By \ Fayez Moawad

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand  # Public attribute
        self.color = color  # Public attribute
        self._service_schedule = "Every 6 months"  # Protected attribute
        self.__engine_number = "12345ABC"  # Private attribute
    
    def display_info(self):
        print(f"This car is a {self.color} {self.brand} from {self.year}.")
    
    def get_engine_number(self):
        # Public method to access the private attribute
        return self.__engine_number

# Creating an object
my_car = Car("Toyota", "Red", 2020)

# Accessing public attributes
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red

# Accessing a protected attribute (not recommended)
print(my_car._service_schedule)  # Output: Every 6 months

# Attempting to access a private attribute directly (will cause an error)
# print(my_car.__engine_number)  # Uncommenting this line causes AttributeError

# Accessing a private attribute through a public method
print(my_car.get_engine_number())  # Output: 12345ABC


# Public Attributes/Methods: Like brand and color, these are accessible from anywhere.
# Protected Attributes: Denoted by a single underscore (e.g., _service_schedule). 
# This signals to the developer that it should not be accessed directly, 
# although Python does not enforce this rule.
# Private Attributes: Denoted by a double underscore (e.g., __engine_number). 
# These are intended to be hidden from outside the class 
# and can only be accessed using methods defined within the class.