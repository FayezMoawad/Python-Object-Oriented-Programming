# Lesson 12: Understanding Static Methods and Class Methods
# Concept: How to Use @staticmethod and @classmethod 
# By \ Fayez Moawad


class Car:
    def __init__(self, brand, year, horsepower):
        self.brand = brand
        self.year = year
        self.horsepower = horsepower

    @staticmethod
    def is_classic(year):
        # Checks if the car is more than 25 years old
        current_year = 2024
        return current_year - year > 25

    @classmethod
    def from_string(cls, car_str):
        # Creates a Car object from a string like "Toyota,2020,300"
        brand, year, horsepower = car_str.split(',')
        return cls(brand, int(year), int(horsepower))

# Using the static method
print(Car.is_classic(1995))  # Output: True (more than 25 years old)

# Using the class method to create an object
car_data = "Honda,2021,250"
new_car = Car.from_string(car_data)
print(new_car.brand)  # Output: Honda
print(new_car.year)   # Output: 2021
print(new_car.horsepower)  # Output: 250


# @staticmethod (is_classic): This method checks if a given year is over 25 years ago. 
# It doesn’t require any instance or class data, so it’s defined as a static method.
# @classmethod (from_string): This method parses a string to create a Car object, 
# making it a factory method. It uses cls to refer to the class, which allows it to create 
# new instances.
