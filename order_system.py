def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    order = []  # Set up order list
    order_total = 0.0  # Initialize order_total
    menu_items = get_menu_items_dict(menu)  # Get the menu items mapped to the menu numbers

    print("Welcome to the Generic Take Out Restaurant.")

    while True:  # Continuous loop for ordering
        print("What would you like to order? ")  # Ask the customer for their order
        print_menu_heading()  # Print menu header
        i = 1  # Initialize menu item number
        # Loop through the menu dictionary
        for food_category, meals in menu.items():
            for meal, price in meals.items():
                print_menu_line(i, food_category, meal, price)  # Print menu item
                i += 1  # Update the menu selection number

        item_number = input("Type menu number: ")
        if item_number.lower() == 'q':  # Exit if the customer wants to quit
            break
        # Validate input and update order
        if item_number.isdigit() and 1 <= int(item_number) < i:  # Check against i, which is the next item number
            order = update_order(order, item_number, menu_items)  # Update the order list
        else:
            print("Invalid item number. Please try again.")
            print(f"{item_number} was not a menu option.")

        continue_ordering = input("Would you like to keep ordering? (N)o to quit: ")
        if continue_ordering.lower() == 'n':  # Check if the customer wants to continue ordering
            print("Thank you for your order!")
            prices_list = [item['Price'] * item['Quantity'] for item in order]  # List comprehension for prices
            order_total = round(sum(prices_list), 2)  # Calculate total price
            break  # Exit the ordering loop

    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered (updated as needed).
    """
    # Check if the customer typed a number
    if menu_selection.isdigit():
        # Convert the menu selection to an integer
        menu_selection = int(menu_selection)

        # Check if the menu selection is valid
        if menu_selection in menu_items:  # Check against the integer keys
            # Store the item details
            item_details = menu_items[menu_selection]
            item_name = item_details["Item name"]
            item_price = item_details["Price"]

            # Ask the customer for the quantity of the menu item
            quantity = input(f"What quantity of {item_name} would you like? \n(This will default to 1 if number is not entered)\n")
            # Check if the quantity is a number, default to 1 if not
            if quantity.isdigit():
                quantity = int(quantity)
            else:
                quantity = 1  # Default to 1 if input is invalid
            # Add a dictionary to the order list 
            # The dictionary should include the item name, price, and quantity
            order.append({
                "Item name": item_name,
                "Price": float(item_price),  # Ensure this is a float
                "Quantity": quantity
            })
        else:
            # When the menu selection wasn't valid:
            print(f"Menu selection {menu_selection} is not valid. Please select a valid menu option.")
    else:
        # When the user's input isn't valid:
        print("Please enter a valid number for the menu selection.")

    # Return the updated order
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Loop through the items in the customer's receipt
    for item in receipt:
        # Store the dictionary items as variables
        item_name = item["Item name"]
        item_price = item["Price"]
        item_quantity = item["Quantity"]

        # Print the receipt line using the print_receipt_line function
        print_receipt_line(item_name, item_price, item_quantity)

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

