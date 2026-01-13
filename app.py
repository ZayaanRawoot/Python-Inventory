# main application with simple menu systems
from inventory.manager import InventoryManager  #when you have a folder this is the structure you use: import folder.filename or from import folder.filename import Class
from inventory.items import * #items is already accessing everything base has so there is no need to import 

def display_menu ():
    """Display the main menu options"""
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Add a Perishable Item")
    print("2. Add Digital Item")
    print("3. Remove Item")
    print("4. Selling Item")
    print("5. View Current Inventory")
    print("6. View Sale History")
    print("7  Print Current Stock")
    print("8. Exit")

    # Create Classes to Achieve all these options


# capture positive integers
def get_pInt(prompt):
    """This is a helper function to get + integers/numbers"""

    while True:
        try:
            value= int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number")
        except:
            print("Please enter a valid number.")


def main():
    """Main program loop"""
    inventory = InventoryManager() # created an object 
    while True:
        display_menu()
        choice = input("Enter an option number(1-8): ")
        if choice == "1":
            # Add perishable
            name = input("Enter item name: ")
            quantity = get_pInt("Enter quantity: ")
            exp = input("Enter Expiry date (YYYY-MM-DD): ")
            inventory.add_item(PerishableItem(name,quantity,exp))
        elif choice == "2":
            # Add perishable
            name = input("Enter item name: ")
            quantity = get_pInt("Enter quantity: ")
            inventory.add_item(DigitalItem(name,quantity))
        elif choice == "3":
            # remove item
            name = input("Enter item name: ")
            inventory.remove_item(name)
        elif choice == "4":
            # sell item
            name = input("Enter item name: ")
            quantity = get_pInt("Enter quantity: ")
            inventory.sell_item(name, quantity) #check out how to print receipt
            
        elif choice == "5":
            # view inventory
            inventory.view_inventory()
        elif choice == "6":
            # view sales
            inventory.view_sold_items()
        elif choice == "7":
            # print stock 
            inventory.print_current_stock()
        elif choice == "8":
            # exit program
            print("Thank you, bye!")
            break
        else:
            print("Invalid choice, please enter an number from 1-8.")

main()

# display_menu()
# name = "apple"
# qty= 3
# price = 2
# print(f"{name.capitalize():<15} {qty:>3} x R1.00 = R{price:.2f}") #2f gives two decimal places 
# # go over splicing