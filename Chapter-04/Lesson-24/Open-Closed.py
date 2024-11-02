# Lesson 24: Understanding the SOLID Principles in Python OOP
# Concept: Open/Closed Principle (OCP):
# By \ Fayez Moawad

# Example Without Applying OCP:
# Imagine you have a program that calculates the area of different shapes. 
# You might start with a simple class like this:

""" class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height
        # More shape types would require adding more `elif` conditions """
        

# Applying OCP:
# To follow OCP, you can use polymorphism to allow new shape types 
# to be added without changing existing code. You can do this by defining 
# a common interface or abstract class for shapes and implementing specific 
# behavior in derived classes.

from abc import ABC, abstractmethod

# Step 1: Create an abstract class or interface for shapes
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Step 2: Implement concrete classes for different shapes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Step 3: Create an AreaCalculator that works with any shape
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def calculate_areas(self):
        for shape in self.shapes:
            print(f"Area: {shape.calculate_area()}")

# Usage example
shapes = [Circle(5), Rectangle(4, 6)]
calculator = AreaCalculator(shapes)
calculator.calculate_areas()



# How This Applies OCP:
# The AreaCalculator class does not need to be modified when new shapes are added. 
# Instead, you create a new class that inherits from Shape and implements 
# the calculate_area() method.
# This design makes your code open for extension (by adding new shape types) 
# but closed for modification (no need to change the AreaCalculator).
# Benefits of OCP:
# Stability: Reduces the risk of breaking existing functionality when adding new features.
# Flexibility: Makes it easier to extend the code with new behavior.
# Maintainability: Encourages cleaner, modular code that is easier 
# to understand and manage.