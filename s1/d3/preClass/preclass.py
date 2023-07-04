# Snack Inventory Management

# Initialize the snack inventory
snack_inventory = []

# Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    snack_price = float(input("Enter the snack price: "))
    snack_available = input("Is the snack available? (yes/no): ")

    snack = {
        "id": snack_id,
        "name": snack_name,
        "price": snack_price,
        "available": snack_available.lower() == "yes"
    }

    snack_inventory.append(snack)
    print("Snack added to the inventory.")

# Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter the snack ID to remove: ")
    snack = find_snack_by_id(snack_id)

    if snack:
        snack_inventory.remove(snack)
        print("Snack removed from the inventory.")
    else:
        print("Snack not found in the inventory.")

# Function to update the availability of a snack
def update_availability():
    snack_id = input("Enter the snack ID to update availability: ")
    snack = find_snack_by_id(snack_id)

    if snack:
        new_availability = input("Is the snack available? (yes/no): ")
        snack["available"] = new_availability.lower() == "yes"
        print("Snack availability updated.")
    else:
        print("Snack not found in the inventory.")

# Function to find a snack by its ID
def find_snack_by_id(snack_id):
    for snack in snack_inventory:
        if snack["id"] == snack_id:
            return snack
    return None

# Function to display the snack inventory
def display_inventory():
    print("Snack Inventory:")
    print("----------------")
    if snack_inventory:
        for snack in snack_inventory:
            print("ID:", snack["id"])
            print("Name:", snack["name"])
            print("Price:", snack["price"])
            print("Availability:", "Yes" if snack["available"] else "No")
            print("----------------")
    else:
        print("No snacks in the inventory.")

# Function to record a snack sale
def record_sale():
    snack_id = input("Enter the snack ID sold: ")
    snack = find_snack_by_id(snack_id)

    if snack:
        if snack["available"]:
            snack["available"] = False
            print("Snack sale recorded.")
        else:
            print("Snack is already sold.")
    else:
        print("Snack not found in the inventory.")

# Main program loop
while True:
    print("Mumbai Munchies - Canteen Management")
    print("-----------------------------------")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. Record Snack Sale")
    print("5. Display Snack Inventory")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        display_inventory()
   
