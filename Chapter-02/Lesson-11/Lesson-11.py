# Lesson 11: Understanding Dunder (Magic) Methods
# Concept: Using Dunder Methods to Add Special Behaviors to Your Classes
# By \ Fayez Moawad

class Car:
    def __init__(self, brand, year, horsepower):
        self.brand = brand
        self.year = year
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.brand} car from {self.year} with {self.horsepower} HP"

    def __add__(self, other):
        if isinstance(other, Car):
            combined_horsepower = self.horsepower + other.horsepower
            return f"Combined horsepower of {self.brand} and {other.brand}: {combined_horsepower} HP"
        raise TypeError("Can only add another Car object")

# Creating Car objects
car1 = Car("Toyota", 2020, 300)
car2 = Car("Honda", 2021, 250)

# Using the __str__ method
print(car1)  # Output: Toyota car from 2020 with 300 HP

# Using the __add__ method
print(car1 + car2)  # Output: Combined horsepower of Toyota and Honda: 550 HP

# Trying to add an incompatible type (raises TypeError)
# print(car1 + "Bike")  # Uncommenting this line raises TypeError


# __str__ Method: Provides a readable string representation of the Car object, 
# making print(car1) output a friendly format.
# __add__ Method: Customizes the + operator to sum the horsepower of two Car 
# objects and return a formatted string. If a non-Car object is added, it raises a TypeError.