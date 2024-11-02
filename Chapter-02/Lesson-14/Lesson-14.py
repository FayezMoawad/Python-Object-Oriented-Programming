# Lesson 14: Chaining Methods in Python OOP
# Concept: Implementing and Using Method Chaining for Fluent Interfaces
# By \ Fayez Moawad


class Car:
    def __init__(self, brand, year, horsepower):
        self.brand = brand
        self.year = year
        self.horsepower = horsepower

    def set_brand(self, brand):
        self.brand = brand
        return self  # Return self for chaining

    def set_year(self, year):
        self.year = year
        return self  # Return self for chaining

    def set_horsepower(self, horsepower):
        self.horsepower = horsepower
        return self  # Return self for chaining

    def display_info(self):
        print(f"{self.brand} car from {self.year} with {self.horsepower} HP")
        return self  # Return self for chaining

# Creating a Car object and chaining methods
car1 = Car("Toyota", 2020, 300)
car1.set_brand("Honda").set_year(2021).set_horsepower(350).display_info()
# Output: Honda car from 2021 with 350 HP



# Method Chaining: The set_brand(), set_year(), and set_horsepower() methods return self, 
# which allows the subsequent method to be called on the same object.
# Fluent Interface: The code reads naturally as 
# car1.set_brand("Honda").set_year(2021).set_horsepower(350).display_info(), 
# making it clear and concise.