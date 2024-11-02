# Lesson 21: Understanding the SOLID Principles in Python OOP
# Concept: The Dependency Inversion Principle (DIP):
# By \ Fayez Moawad

from abc import ABC, abstractmethod

# Step 1: Create an interface (abstract class) for the payment service
class PaymentService(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Step 2: Implement concrete classes for different payment services
class PayPalPaymentService(PaymentService):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal.")

class StripePaymentService(PaymentService):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through Stripe.")

# Step 3: Create a high-level module that depends on the abstraction
class OrderProcessor:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def process_order(self, amount):
        print("Starting order processing...")
        self.payment_service.process_payment(amount)
        print("Order processed successfully!")

# Step 4: Demonstrate dependency inversion by injecting different payment services
# Using PayPal service
paypal_service = PayPalPaymentService()
order_processor = OrderProcessor(paypal_service)
order_processor.process_order(100)

print("\nSwitching to a different payment service:\n")

# Using Stripe service
stripe_service = StripePaymentService()
order_processor = OrderProcessor(stripe_service)
order_processor.process_order(200)



# PaymentService: This is the abstract class (interface) that defines the method 
# process_payment(), which high-level modules depend on.
# PayPalPaymentService and StripePaymentService: These are the concrete 
# implementations of PaymentService.
# OrderProcessor: This is the high-level module that depends on the PaymentService interface, 
# not on the specific implementations.
# By changing the concrete payment service passed to OrderProcessor, 
# we demonstrate how the high-level module does not need to be altered to use different 
# low-level modules, following the Dependency Inversion Principle.