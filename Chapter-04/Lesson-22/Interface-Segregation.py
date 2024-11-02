# Lesson 22: Understanding the SOLID Principles in Python OOP
# Concept: The Interface Segregation Principle (ISP):
# By \ Fayez Moawad

# To follow ISP, split the larger interface into smaller, 
# more specific ones that cater to the needs of different clients.

class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self, document):
        pass

class Fax:
    def fax_document(self, document):
        pass


# Now, you can create classes that only implement the methods they need:

# class SimplePrinter use only Printer interface
class SimplePrinter(Printer):
    def print_document(self, document):
        print("Printing document...")

# class AdvancedPrinter use Printer, Scanner and Fax interfaces
class AdvancedPrinter(Printer, Scanner, Fax):
    def print_document(self, document):
        print("Printing document...")

    def scan_document(self, document):
        print("Scanning document...")

    def fax_document(self, document):
        print("Faxing document...")


