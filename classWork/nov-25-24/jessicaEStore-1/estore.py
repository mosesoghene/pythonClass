import os

MENU = """

    1. View Products
    2. Add item to cart
    3. Remove from cart
    4. View cart
    5. Checkout
    6. Exit
    
    Select option:
    > """

products = {
    'names': ["laptop", "phone", "headphones"],
    'prices': [1000, 500, 100]
}

cart = {
    'names': [],
    'prices': []
}

def view_products():
    for index in range(len(products['names'])):
        print(f"\t{products['names'][index]} -> {products['prices'][index]}")

def add_to_cart(cart, product):
    if product in cart['names']:
        cart['names'].append(product.capitalize())
        cart['prices'].append(products['prices'][products['names'].index(product.lower())])
        print(f"{product.upper()} has been added to cart \n")
    return cart

def remove_from_cart(cart, product):
    if product in cart['names']:
        cart['names'].remove(product.capitalize())
        cart['prices'].remove(products['prices'][products['names'].index(product.lower())])
        print(f"{product.upper()} has been removed from cart \n")
    else:
        print("\nItem not in cart")
    return cart

def view_cart():
    for index in range(len(cart['names'])):
        print(f"\t{cart['names'][index]} -> ${cart['prices'][index]}")

def checkout(cart):
    total = 0
    for price in cart['prices']:
        print(f"{cart['names'][cart['prices'].index(price)]} \t| ${price}")
        total += price
    print(f"Total : ${total}")


print("Welcome to Jessica's E-Store")

running = True
while running:
    user_response = input(MENU)
    match (user_response):
        case "1":
            print("\nAll Available Products:") 
            view_products()
        case "2": 
            option = input("To add to cart, Enter product name > ")
            cart = add_to_cart(cart, option)
        case "3": 
            option = input("To remove from cart, enter product name > ")
            cart = remove_from_cart(cart, option)
        case "4":
            view_cart()
        case "5": 
            checkout(cart)
        case "6" : running = False
    
    

