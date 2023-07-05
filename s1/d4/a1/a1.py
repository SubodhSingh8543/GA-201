import sys

# Step 1: Set up initial data structures
menu = []
orders = {}
order_id_counter = 1

# Step 2: Implement menu management features
def add_dish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ").lower()
    
    menu.append({
        "dish_id": dish_id,
        "dish_name": dish_name,
        "price": price,
        "availability": availability
    })
    print(f"{dish_name} has been added to the menu.")

def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")
    
    for dish in menu:
        if dish["dish_id"] == dish_id:
            menu.remove(dish)
            print(f"Dish with ID {dish_id} has been removed from the menu.")
            return
    
    print(f"No dish found with ID {dish_id}.")

def update_availability():
    dish_id = input("Enter the dish ID to update availability: ")
    availability = input("Is the dish available? (yes/no): ").lower()
    
    for dish in menu:
        if dish["dish_id"] == dish_id:
            dish["availability"] = availability
            print(f"Availability for dish with ID {dish_id} has been updated.")
            return
    
    print(f"No dish found with ID {dish_id}.")

# Step 3: Implement order management features
def take_order():
    global order_id_counter
    customer_name = input("Enter customer name: ")
    order = {"order_id": order_id_counter, "customer_name": customer_name, "status": "received", "dishes": []}
    
    while True:
        dish_id = input("Enter the dish ID (or press Enter to finish): ")
        if dish_id == "":
            break
        
        dish = find_dish(dish_id)
        if dish is None:
            print(f"No dish found with ID {dish_id}.")
        elif dish["availability"] == "yes":
            order["dishes"].append(dish)
            print(f"{dish['dish_name']} added to the order.")
        else:
            print(f"{dish['dish_name']} is not available.")
    
    if len(order["dishes"]) > 0:
        orders[order_id_counter] = order
        order_id_counter += 1
        print("Order placed successfully!")

def find_dish(dish_id):
    for dish in menu:
        if dish["dish_id"] == dish_id:
            return dish
    return None

# Step 4: Implement order status update feature
def update_order_status():
    order_id = int(input("Enter the order ID to update status: "))
    status = input("Enter the new status: ")
    
    if order_id in orders:
        orders[order_id]["status"] = status
        print(f"Order {order_id} status updated to {status}.")
    else:
        print(f"No order found with ID {order_id}.")

# Step 5: Implement review orders feature
def review_orders():
    print("Orders:")
    for order_id, order in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Status: {order['status']}")
        print("Dishes:")
        for dish in order["dishes"]:
            print(f"- {dish['dish_name']}")
        print()

# Step 6: Implement error handling and edge cases
def handle_error():
    print("Invalid choice. Please try again.")

# Step 7: Implement exit feature
def exit_system():
    print("Thank you for using Zesty Zomato. Have a great day!")
    return

# Main program loop
while True:
    print("Welcome to Zesty Zomato!")
    print("1. Add Dish")
    print("2. Remove Dish")
    print("3. Update Dish Availability")
    print("4. Take Order")
    print("5. Update Order Status")
    print("6. Review Orders")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_dish()
    elif choice == "2":
        remove_dish()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        take_order()
    elif choice == "5":
        update_order_status()
    elif choice == "6":
        review_orders()
    elif choice == "7":
        exit_system()
    else:
        handle_error()
