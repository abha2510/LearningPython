import datetime

snacks = []

class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

def add_snack():
    snack_id = int(input("Enter snack ID: "))
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Enter snack availability (yes/no): ")
    snack = Snack(snack_id, name, price, availability.lower() == "yes")
    snacks.append(snack)
    print(f"Added {snack.name} to the inventory.")

def remove_snack():
    snack_id = int(input("Enter snack ID to remove: "))
    for snack in snacks:
        if snack.snack_id == snack_id:
            snacks.remove(snack)
            print(f"Removed {snack.name} from the inventory.")
            return
    print("Snack not found in the inventory.")

def update_snack_availability():
    snack_id = int(input("Enter snack ID to update availability: "))
    availability = input("Enter new availability (yes/no): ")
    for snack in snacks:
        if snack.snack_id == snack_id:
            snack.availability = availability.lower() == "yes"
            print(f"Updated availability of {snack.name} to {availability}.")
            return
    print("Snack not found in the inventory.")

def display_inventory():
    print("Snack Inventory:")
    for snack in snacks:
        print(f"ID: {snack.snack_id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.availability}")

def make_sale():
    snack_id = int(input("Enter snack ID: "))
    quantity = int(input("Enter quantity sold: "))

    snack = None
    for s in snacks:
        if s.snack_id == snack_id:
            snack = s
            break

    if snack is None:
        print("Snack not found in the inventory.")
        return

    if not snack.availability:
        print("Snack is not available for sale.")
        return

    if quantity <= 0:
        print("Invalid quantity. Please enter a positive value.")
        return

    if quantity > get_available_quantity(snack):
        print("Insufficient quantity available.")
        return

    timestamp = datetime.datetime.now()
    sale = SalesRecord(snack, quantity, timestamp)
    update_inventory(snack, quantity)
    print(f"Sale made: {quantity}x {snack.name}")

def get_available_quantity(snack):
    sold_quantity = sum(sale.quantity for sale in sales_records if sale.snack == snack)
    return snack.quantity - sold_quantity

def update_inventory(snack, quantity):
    snack.availability = False
    print(f"Inventory updated: {snack.name} - {quantity} sold.")

def display_sales_records():
    print("Sales Records:")
    for sale in sales_records:
        snack = sale.snack
        quantity = sale.quantity
        timestamp = sale.timestamp
        print(f"Timestamp: {timestamp}, Snack: {snack.name}, Quantity: {quantity}")


class SalesRecord:
    def __init__(self, snack, quantity, timestamp):
        self.snack = snack
        self.quantity = quantity
        self.timestamp = timestamp

sales_records = []

def display_menu():
    print("Canteen Management System Menu:")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update the availability of a snack")
    print("4. Make a sale")
    print("5. Display snack inventory")
    print("6. Display sales records")
    print("7. Quit")

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_snack_availability()
    elif choice == "4":
        make_sale()
    elif choice == "5":
        display_inventory()
    elif choice == "6":
        display_sales_records()
    elif choice == "7":
        print("Quitting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
