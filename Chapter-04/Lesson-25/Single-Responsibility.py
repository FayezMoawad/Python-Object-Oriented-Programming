# Lesson 25: Understanding the SOLID Principles in Python OOP
# Concept: Single Responsibility Principle (SRP):
# By \ Fayez Moawad

# Example Without SRP:
# Imagine a class that handles user data:

""" class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        # Code to save the user to the database
        print(f"Saving {self.name} to the database...")

    def send_welcome_email(self):
        # Code to send a welcome email to the user
        print(f"Sending welcome email to {self.email}...") """

# Problems:

# The User class has two responsibilities: managing user data and handling 
# database operations and email notifications.
# If changes are required in how the email is sent or how the data is stored, 
# modifying the User class may affect its other responsibilities.


# Applying SRP:
# To follow SRP, split the responsibilities into separate classes so that 
# each class has a single reason to change.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save_to_database(self, user):
        # Code to save the user to the database
        print(f"Saving {user.name} to the database...")

class EmailService:
    def send_welcome_email(self, user):
        # Code to send a welcome email to the user
        print(f"Sending welcome email to {user.email}...")




# How This Applies SRP:
# User class: Manages only the user's data.
# UserRepository class: Responsible for database operations.
# EmailService class: Handles email-related functionality.
# Benefits of SRP:
# Improved Maintainability: Changes to one responsibility do not affect
# other parts of the code.
# Easier to Understand: Each class has a clear and distinct role.
# Better Testability: Smaller, more focused classes are easier to test independently.
# Real-World Analogy:
# Think of SRP like a department in a company. If you have one person 
# handling accounting, customer service, and IT support, it becomes chaotic 
# when changes are needed in any of those areas. It's better to have one person 
# (or team) for each task so that changes and responsibilities are managed efficiently.