"""Inventory management system that handles all operations"""
from inventory.items import * # "*" imports all # we want to import PersihableItem, DigitalItem
# the reason we dont take from base is bc items is inheriting everything from base
from datetime import datetime

class InventoryPrinter:
    """Handle printing inventory and receipts to files"""

    # static methods 
    @staticmethod
    def print_stock(inventory, filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"):
        """Print current inventory to a text file"""
        with open(filename, "w") as f:#create the file
            f.write("===   CURRENT INVENTORY   ===")
            f.write(f"\nGenerated:{datetime.now()}\n\n")

            if not inventory:
                f.write("inventory is empty")
            else:
                for item in inventory.values():
                    f.write(f"{str(item)}\n")
            f.write("\n==== END OF RECEIPT ====\n")
        with open(filename,"r") as f:
            
            print(f.read())
        print (f"Stock report saved to file {filename}")

    @staticmethod
    def print_receipt(items_sold, filename = f"Receipt_{str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.txt"):
        """Print current inventory to a text file"""
        with open(filename, "w") as f:#create the file
            f.write("===   RECEIPT   ===\n")
            f.write(f"Date:{datetime.now()}\n\n")
            f.write("ITEMS PURCHASED  ")
            

            total=0
            for name, qty in items_sold.items():
                price = qty * 1.00
                total += price
                f.write(f"{name.capitalize():<15} {qty:>3} x R1.00 = R{price:.2f}") #2f gives two decimal places 
            f.write("\n")
            f.write(f"TOTAL: R{total:.2f}")
            f.write("\n==== THANK YOU FOR YOUR PURCHASE ====\n\n")
        with open(filename,"r") as f:
            
            print(f.read())
            
        print (f"Stock report saved to file {filename}")




class InventoryManager:
    """Main inventory management system"""
    # will demonstrate logic and state management
    def __init__(self):
        """Initialize empty inventory"""
        self.inventory = {}
        self.sold_items = []

    def add_item(self,item):
        """Add an item to inventory or update quantity if the item already exists"""
        name = item.get_name()

        if name in self.inventory:
            self.inventory[name].add_quantity(item.get_quantity())
        else:
            self.inventory[name] = item
    
        print(f"Added {item.get_quantity()} {name}(s)")

    def remove_item(self, name):
        """Completely remove an item from your inentory"""
        name = name.lower()

        if name in self.inventory:
            del self.inventory[name]
            print(f"Removed {name.capitalize()}")
        else:
            print(f"{name} not found.")

    def sell_item(self, name, quantity):
        """Sell items and track sales
        Return:
                True if sale was successful, False otherwise
        """
        name = name.lower()

        if name not in self.inventory:
            print(f"{name} not found.")
            return False
        
        if quantity > self.inventory[name].get_quantity():
            available = self.inventory[name].get_quantity()
            print(f"Not enough {name} in stock. Only {available} available.")
            return False

        removed = self.inventory[name].remove_quantity(quantity)

        if removed > 0:
            self.sold_items.append((name, removed))#use tuple for multiple values in append . removed here is the qauntity
            # print(f"Sold {removed} {name}(s)") #[("apple", 5),("banana", 2)] - the above is creating a list of tuples
            #       Sold     5     apple (s)
            # Check if we need to print a receipt 
            if input("Print receipt Y/N?").lower() == "y":

                InventoryPrinter.print_receipt({name:removed})
            
            if self.inventory[name].get_quantity() == 0:
                print(f"{name} is now out of stock")
                return True
            else:
                print(f"\n{name.capitalize()} has {self.inventory[name].get_quantity()} item(s) left in stock")
                return False
    
    def print_current_stock(self):
        """Print the current stock levels/ inventory to a file"""

        InventoryPrinter.print_stock(self.inventory)

    def view_inventory(self):
        """Display current inventory to console"""

        if not self.inventory :
            print("Inventory is empty")
        else:
            print(f"\n----- Current Inventory -----")
            for item in self.inventory.values():
                print(item)

    def view_sold_items(self):
        """Display sales history to the console"""
        """Display current inventory to console"""
        if not self.sold_items :
            print("No items sold yet.")
        else:
            print(f"\n----- Sales History -----")
            for name,qty in self.sold_items: #sold items is a list of tuples , first access index then value 
                print(f"{name.capitalize()}: {qty} sold.")
                #          Apple           :   4   sold.



# In order to fix the issues , .strftime('%Y-%m-%d_%H-%M-%S') had to be added to the file name and the receipt data had to be parsed as a dictionary , not InventoryPrinter.print_receipt([name,removed]) and added f.read to read the file and print it to the console. the inventory when printed always returned out of stock, so i changed the else statement in line 102 of manager.py , to show how many items are left in stock
