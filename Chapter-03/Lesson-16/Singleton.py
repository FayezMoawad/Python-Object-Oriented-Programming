# Lesson 16: Understanding Design Patterns in Python OOP
# Concept: Singleton Pattern by \ Fayez Moawad


# The Singleton pattern ensures that a class has only one instance. 
# This is useful for classes that handle shared resources such as a configuration 
# manager or database connection.
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Creating Singleton objects
singleton1 = Singleton()
singleton2 = Singleton()

# Verifying that both variables point to the same instance
print(singleton1 is singleton2)  # Output: True


# __new__ Method: Used to control object creation. 
# The first time the Singleton class is instantiated, 
# it creates a new instance. Subsequent calls return the existing instance.
# Single Instance: This ensures there is only one instance 
# of the class throughout the application.

# Singleton: Ensures a class has only one instance and provides a global point of access.