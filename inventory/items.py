from inventory.base import Item

"""Concrete item classes that inherit from base item class"""

class PerishableItem(Item):
    """A perishable item that has an expiration date """

    def __init__(self, name, quantity, exp_date):
        super().__init__(name, quantity)#initilaize parent class
        self.exp_date = exp_date

    def get_type(self):
        """Returns item type(Implementation of abstract method)"""
        
        return "Perishable"
    
    def __str__(self):
        return f"{super().__str__()} | Expires: {self.exp_date}"
    
    
class DigitalItem(Item):
    """A digital item does not have physical stock. Shows simple inheritance without additional attributes."""
    # def __init__(self, name , quantity):
    #     super().__init__(name, quantity)#no need to initialize again , unless you have additional attributes because it inherits the initialisation

    def get_type(self):
        return 'Digital'
    
    def __str__(self):
        return f"{super().__str__()} | Downloadable"