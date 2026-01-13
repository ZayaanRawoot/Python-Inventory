# This will act as our parent module
"""This module contains the base Item class that all other items will inherit from"""

from abc import ABC, abstractmethod


# classes have to start with caps , dont have to put parethensis, you can but not necessary unless you are inheriting 
class Item(ABC):
    """Abstract base class for all inventory items"""

    # Attributes -data 
    def __init__(self, name, quantity):
        # stores name in lowercase for consistency 
        self.name = name.lower()
        # Stores quantity of the items
        self.quantity=quantity

    # Methods- functions that work with the above data
    def add_quantity(self, amount):
        """Increase item quantity by specified amount"""
        if amount > 0:
            self.quantity += amount
        else:
            print("Amount must be positive")

    def remove_quantity(self, amount):
        """Decrease item quantity"""
        if amount <= 0:
            print("Amount must be positive")
            return 0
        
        removed = min(amount, self.quantity) #can't remove more than we have . min returns the smallest number in an iterable. will return the smallest number between the two: min(amount, self.quantity)
        # removed is going to compare the amt we want to remove and the amount that we have 
        self.quantity -= removed
        return removed

    def get_quantity(self):
        """Get the current quantity in stock"""
        return self.quantity
    
    def get_name(self):
        """Get the item's name"""
        return self.name
    
    def __str__(self): #returns a string representation of whatever arguments/parameters you feed it . str is a magic method
        """String representation of the item for display"""
        return f"{self.name.capitalize()} ({self.get_type()}): {self.quantity}"

    # Abstract Method
    # forces children that inherit form parents to use specific method 
    
    # use decorator, then create abstarct class
    @abstractmethod
    def get_type(self):
        """Abstract method that child classes must implement"""#every child class must implement this method, otherwise it must not inherit this class "Base" at all
        pass