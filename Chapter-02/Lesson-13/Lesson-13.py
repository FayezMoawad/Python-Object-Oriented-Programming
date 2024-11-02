# Lesson 13: Operator Overloading with Dunder Methods
# Concept: Customizing How Python Operators Behave with Your Classes
# By \ Fayez Moawad

class Car:
    def __init__(self, brand, year, horsepower):
        self.brand = brand
        self.year = year
        self.horsepower = horsepower

    def __add__(self, other):
        if isinstance(other, Car):
            combined_hp = self.horsepower + other.horsepower
            return f"Combined horsepower of {self.brand} and {other.brand}: {combined_hp} HP"
        raise TypeError("Addition is only supported between Car objects")

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.horsepower == other.horsepower
        return False

    def __str__(self):
        return f"{self.brand} car from {self.year} with {self.horsepower} HP"

# Creating Car objects
car1 = Car("Toyota", 2020, 300)
car2 = Car("Honda", 2021, 300)
car3 = Car("Ford", 2019, 400)

# Using the overloaded + operator
print(car1 + car3)  # Output: Combined horsepower of Toyota and Ford: 700 HP

# Using the overloaded == operator
print(car1 == car2)  # Output: True (both have the same horsepower)
print(car1 == car3)  # Output: False

# Displaying the car using the __str__ method
print(car1)  # Output: Toyota car from 2020 with 300 HP


# __add__ Method: Redefines the + operator to add the horsepower of two Car objects 
# and return a formatted string.
# __eq__ Method: Redefines the == operator to compare the horsepower of two Car objects.
# __str__ Method: Allows print(car1) to display a friendly string representation.