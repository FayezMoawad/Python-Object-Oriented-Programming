# Lesson 3: Creating Methods in a Class
# Concept: Defining and Using Methods in a Class by \ Fayez Moawad


class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    
    def display_info(self):
        print(f"This car is a {self.color} {self.brand} from {self.year}.")
    
    def start_engine(self):
        print(f"The {self.brand} engine is now running.")
    
    def stop_engine(self):
        print(f"The {self.brand} engine has been turned off.")
    
    def check_age(self, current_year):
        age = current_year - self.year
        return age


# Creating an object and using its methods
my_car = Car("Toyota", "Red", 2020)
my_car.display_info()   # Output: This car is a Red Toyota from 2020.
my_car.start_engine()   # Output: The Toyota engine is now running.
my_car.stop_engine()    # Output: The Toyota engine has been turned off.

# Check the age of the car
car_age = my_car.check_age(2024)
print(f"My car is {car_age} years old.")  # Output: My car is 4 years old.


# We defined three methods: display_info(), start_engine(), and stop_engine().
# Each method takes self to access and work with the instance's attributes.
# You can call these methods on the my_car object using the dot notation, like
# my_car.start_engine().
# check_age() method to determine the car's age:
# Adding More Logic: Methods can include logic that manipulates 
# the attributes of the instance or returns data. 