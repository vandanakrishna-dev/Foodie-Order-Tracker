# Define the menu as a dictionary where the keys are dish names and values are their prices
menu = {
    "Tomato Soup": 60,
    "Vegetarian Pizza": 80,
    "Grilled Chicken": 120,
    "Chocolate Lava Cake": 160,
    "Apple Pie": 70,
    "Iced Tea": 90,
    "Espresso": 80,
    "Mango Smoothie": 100,
}

# Print a welcome message to the user
print("Welcome to Flavor Trails Restaurant!")

# Display the menu by iterating through the dictionary
print("Menu:")
for item, price in menu.items():
    # Print each menu item with its price
    print(f"{item}: {price} Rs.")

# Initialize a variable to keep track of the total order amount
order_total = 0

# Define a helper function to take user input and validate it against the menu
def get_item_input(prompt):
    """Helper function to take case-insensitive input and validate against the menu."""
    # Get user input, strip extra spaces, and title-case it to match the menu keys
    item_name = input(prompt).strip().title()
    # Check if the input matches any item in the menu
    if item_name in menu:
        return item_name  # Return the item name if it's valid
    else:
        # Print a message if the item is not on the menu
        print(f"Sorry, {item_name} is not on the menu.")
        return None  # Return None if the input is invalid

# Prompt the user to specify the first dish they want to order
item_one = get_item_input("Please specify the name of the dish you'd like to order: ")
if item_one:  # If the user entered a valid menu item
    # Add the price of the selected item to the total order amount
    order_total += menu[item_one]
    # Print confirmation of the item added
    print(f"You've added {item_one} to your order.")

# Use a loop to allow the user to add more items until they decide to stop
while True:
    # Ask the user if they want to add more items
    another_item = input("Would you like to add something else? (yes/no): ").strip().lower()
    if another_item == "yes":  # If the user wants to add more items
        # Prompt the user to specify another dish
        item_two = get_item_input("Please specify the name of the dish you'd like to order: ")
        if item_two:  # If the input is valid
            # Add the price of the additional item to the total order amount
            order_total += menu[item_two]
            # Print confirmation of the item added
            print(f"You've added {item_two} to your order.")
    elif another_item == "no":  # If the user doesn't want to add more items
        break  # Exit the loop
    else:
        # If the input is invalid, prompt the user to respond with 'yes' or 'no'
        print("Please respond with 'yes' or 'no'.")

# Print the total amount the user needs to pay for their order
print(f"The total amount you need to pay is {order_total} Rs.")
