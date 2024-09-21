import re
# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    return sorted_products  # return for testing

def display_products(products_list):
    for category, items in products.items():
        print(f"\nCategory: {category}")
        display_sorted_products(items)


def display_categories():
    categories = list(products.keys())
    print("Available Categories:")
    for i, category in enumerate(categories):
        print(f"{i + 1}. {category}")

    try:
        choice = int(input("Select a category by number: ")) - 1
        if 0 <= choice < len(categories):
            return choice
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def add_to_cart(cart, product, quantity):
    for i, (prod_name, price, qty) in enumerate(cart):
        if prod_name == product[0]:
            cart[i] = (prod_name, price, qty + quantity)
            return
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    total_cost = 0
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
        total_cost += price * quantity
    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Shipping Address: {address}")
    print("\nItems Purchased:")
    for product, quantity in cart.items():
        price = products[product] * quantity
        print(f"{product}: {quantity} @ ${products[product]:.2f} each - ${price:.2f}")
    print(f"\nTotal Cost: ${total_cost:.2f}")
    print("\nThank you for shopping with us!")

def validate_name(name):
    parts = name.split()
    return len(parts) > 1 and all(part.isalpha() for part in parts)

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-.]+)?$'

    # Match the regex pattern with the input email using re.match
    return re.match(email_regex, email) is not None


def main():
    cart = {}
    print("Welcome to the store!")

    while True:
        print("\nWhat would you like to do?")
        print("1. View Categories")
        print("2. View Products in a Category")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            display_categories()

        elif choice == "2":
            display_categories()
            category = input("\nEnter the category name: ").strip()
            if category in products:
                display_sorted_products(products[category])
            else:
                print("Invalid category.")

        elif choice == "3":
            display_categories()
            category = input("\nEnter the category name: ").strip()
            if category in products:
                display_sorted_products(products[category])
                product_name = input("Enter the product name: ").strip()
                for item in products[category]:
                    if item[0].lower() == product_name.lower():
                        quantity = int(input(f"How many {item[0]}s would you like to add? "))
                        add_to_cart(cart, item[0], quantity)
                        print(f"Added {quantity} {item[0]}(s) to your cart.")
                        break
                else:
                    print("Product not found in the selected category.")
            else:
                print("Invalid category.")

        elif choice == "4":
            display_cart(cart)

        elif choice == "5":
            if not cart:
                print("Your cart is empty.")
                continue
            name = input("Enter your name: ").strip()
            if not validate_name(name):
                print("Invalid name.")
                continue
            email = input("Enter your email: ").strip()
            if not validate_email(email):
                print("Invalid email.")
                continue
            address = input("Enter your shipping address: ").strip()
            total_cost = display_cart(cart)
            generate_receipt(name, email, cart, total_cost, address)
            break

        elif choice == "6":
            print("Thank you for visiting the store!")
            break

        else:
            print("Invalid choice. Please try again.")


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
