# Lesson 23: Understanding the SOLID Principles in Python OOP
# Concept: Liskov Substitution Principle (LSP):
# By \ Fayez Moawad

# Example Without Applying LSP:
# Imagine you have a base class Bird with a method fly() representing flying behavior:

""" 
class Bird:
    def fly(self):
        print("This bird is flying")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly") 
"""
# If you substitute a Bird object with a Penguin object, 
# it will cause problems because Penguin changes the expected behavior of fly().
# Violating LSP: Using a Penguin where a Bird is expected breaks the code.

# Applying LSP:
""" 
To follow LSP correctly, derived classes should be compatible with the base class 
without altering the expected behavior. In the previous example, you can redesign 
the code so that not all birds use the fly() method if some cannot fly. 
"""

class Bird:
    def make_sound(self):
        print("This bird is making a sound.")

class FlyingBird(Bird):
    def fly(self):
        print("This bird is flying.")

class Penguin(Bird):
    def make_sound(self):
        print("Penguins make a sound, but can't fly.")
