# Lesson 6: Getters, Setters, and Property Decorators
# Concept: Using Getters, Setters, and @property to Control Access
# By \ Fayez Moawad


class Car:
    def __init__(self, brand, color, year):
        self._brand = brand      # Protected attribute
        self._color = color      # Protected attribute
        self._year = year        # Protected attribute

    # Getter for brand
    @property
    def brand(self):
        return self._brand

    # Setter for brand
    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value.isalpha():
            self._brand = value
        else:
            raise ValueError("Brand must be a valid string.")

    # Getter for color
    @property
    def color(self):
        return self._color

    # Setter for color
    @color.setter
    def color(self, value):
        if isinstance(value, str) and value.isalpha():
            self._color = value
        else:
            raise ValueError("Color must be a valid string.")
    
    # A calculated property (read-only)
    @property
    def age(self):
        current_year = 2024
        return current_year - self._year

# Creating an object and using getters and setters
my_car = Car("Toyota", "Red", 2020)

# Accessing the brand and color using getters
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red

# Modifying the brand using the setter
my_car.brand = "Honda"
print(my_car.brand)  # Output: Honda

# Accessing the read-only property
print(f"The car's age is {my_car.age} years.")  # Output: The car's age is 4 years.

# Attempting to set an invalid value (will raise an error)
# my_car.color = "1234"  # Uncommenting this line will raise ValueError


# The @property decorator makes the brand and color methods behave like attributes, 
# allowing you to use my_car.brand instead of my_car.brand().
# The @brand.setter method adds validation logic to ensure the brand is a string.
# The age property is read-only because there is no corresponding @age.setter. 
# It calculates the car's age based on the current year.
# Why Use Getters and Setters?:

# They provide control over how attributes are accessed and modified.
# You can include logic such as validation and calculation, making your code 
# safer and more predictable.