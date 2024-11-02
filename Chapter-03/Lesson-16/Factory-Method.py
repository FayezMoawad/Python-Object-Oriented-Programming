# Lesson 16: Understanding Design Patterns in Python OOP
# Concept: Factory Method Pattern by \ Fayez Moawad


# The Factory Method pattern provides an interface for creating objects 
# but allows subclasses to alter the type of objects that are created.

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Using the factory method
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!


# Factory Method: The create_animal method encapsulates the logic of object 
# creation and allows for adding new types of animals without changing the client code.
# Flexibility: Easily extendable to add new types of animals by modifying only the factory method.

# Factory Method: Defines an interface for creating an object but lets subclasses 
# alter the type of objects created.