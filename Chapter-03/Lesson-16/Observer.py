# Lesson 16: Understanding Design Patterns in Python OOP
# Concept: Observer Pattern by \ Fayez Moawad

# The Observer pattern allows an object (the subject) to notify 
# multiple observers of state changes.


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        print("Observer received an update!")

# Implementing the pattern
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify()  # Output: Observer received an update! (twice)


# Subject Class: Maintains a list of observers and notifies them of changes.
# Observer Class: Implements an update method that gets called when the subject is updated.
# Decoupling: The observer pattern helps decouple the subject and its observers, making 
# the code more modular and flexible.
# Benefits of Design Patterns:
# Reusability: Solutions can be adapted to different projects.
# Consistency: Provides a standardized approach to solving design challenges.
# Maintainability: Improves the readability and structure of the code.
# Design patterns offer established solutions for common 
# coding problems, making code easier to understand, extend, and maintain. 
# By understanding when and how to use these patterns, 
# you can write cleaner and more efficient code.