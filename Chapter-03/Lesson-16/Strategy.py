# Lesson 16: Understanding Design Patterns in Python OOP
# Concept: Strategy Pattern by \ Fayez Moawad


# The Strategy pattern is a behavioral design pattern that enables selecting 
# an algorithm’s behavior at runtime. It defines a family of algorithms, 
# encapsulates each one, and makes them interchangeable. This pattern allows 
# the algorithm to vary independently from clients that use it, making the code 
# more flexible and maintainable.

# Key Concepts:
# Encapsulation of Algorithms:
# Different strategies (algorithms) are encapsulated in separate classes, 
# allowing them to be used interchangeably.
# Interface for Strategy:
# A common interface is defined, so each strategy class follows the same structure.
# Context Class:
# Maintains a reference to a strategy object and allows clients to change the strategy at runtime.


from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategy 1: Credit Card Payment
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

# Concrete Strategy 2: PayPal Payment
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

# Context Class
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount):
        self._strategy.pay(amount)

# Using the strategy pattern
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

processor = PaymentProcessor(credit_card_payment)
processor.process_payment(100)  # Output: Paid 100 using Credit Card.

# Changing strategy at runtime
processor.set_strategy(paypal_payment)
processor.process_payment(200)  # Output: Paid 200 using PayPal.




# PaymentStrategy Class: Defines the interface for payment strategies.
# Concrete Strategies (CreditCardPayment, PayPalPayment): Implement the pay method 
# for their specific behavior.
# PaymentProcessor Class: Acts as the context, holding a reference to the PaymentStrategy 
# and allowing the strategy to be changed dynamically.
# Benefits of the Strategy Pattern:
# Flexibility: Allows switching between different algorithms at runtime without 
# modifying the client code.
# Open/Closed Principle: You can introduce new strategies without changing existing code.
# Decoupling: Separates the algorithm's implementation from the client using it, 
# making it easier to maintain and extend.
# Real-World Use Cases:

# Payment processing systems (as shown above).
# Sorting algorithms that can be chosen based on data type or size.
# Game development for different movement or attack behaviors.
# When to Use the Strategy Pattern:
# When you have multiple related algorithms that need to be interchangeable.
# When a class has multiple conditional statements that determine which behavior to use 
# (e.g., if-elif-else chains).
# When you need to isolate the client from the details of different algorithms.
# The Strategy pattern allows for cleaner, more maintainable code 
# by enabling the dynamic change of behavior without altering the context class. 
# This pattern is essential when designing flexible systems that may need 
# different approaches for a task.