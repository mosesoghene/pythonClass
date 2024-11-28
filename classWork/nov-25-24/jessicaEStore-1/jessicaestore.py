import os

MENU = """
    Main Menu
    1. View Products
    2. Add item to cart
    3. Remove from cart
    4. View cart
    5. Checkout
    6. Exit
    
    Select option:
    > """

products = [
    {'laptop': 1000},
    {'phone': 500},
    {'headphones': 100}
]

cart = []

def view(products: list):    
    print(f"\n\033[1m PRODUCT CATALOGUE \033[0m\n")
    for product in products:
        for item in product:
            data = f"\033[1m{item.capitalize():<10}\033[0m ->, ${product[item]}"
            print(data)
            print("-" * len(data))


def add_to(item, cart: list):
    for product in products:
        for key in product:
            if item.lower() == key:
                cart.append({key : product[key]})
        
    return cart


def view_cart(cart: list):
    print(f"\n\033[1m SHOPPING CART \033[0m\n")
    for product in cart:
        for item in product:
            data = f"\033[1m{item.capitalize():<10}\033[0m ->, ${product[item]}"
            print(data)
            print("-" * len(data))



def remove_item(item, cart: list):
    for product in cart:
        for key in product:
            if item.lower() == key:
                cart.remove(product)
        
    return cart
    

def checkout(cart: list):
    total = 0
    for product in cart:
        for price in product.values():
            total += price
        
    return total


program_loop_running = True

while program_loop_running:

    menu_option = input(MENU)
    match menu_option:
        case "1":
            view(products)
        case "2":
            item = input("Enter product name ONLY >> ")
            cart = add_to(item, cart)
        case "3":
            item = input("Enter product name ONLY >> ")
            cart = remove_item(item, cart)
            view_cart(cart)
        case "4":
            view_cart(cart)
        case "5":
            print("$", checkout(cart))
        case "6":
            print("Thanks for shopping")
            program_loop_running = False
    

