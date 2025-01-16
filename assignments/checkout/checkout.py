from datetime import datetime
import os

cart = []

customer_name = input("Enter customer name \n> ")

def add_product_to(cart, product, quantity, price):
    cart.append({'product': product, 'quantity': quantity, 'price': price})
    return cart

def print_invoice(cart):
    os.system("clear")
    print(header_info)
    print("+-----------------+------------+------------+------------+")
    print("|       ITEM      |    QTY     |    PRICE   | TOTAL(NGN) |")
    print("+-----------------+------------+------------+------------+")



    for product_detail in cart:
        print(f"| {product_detail['product']:<15} | {product_detail['quantity']:>10} | {product_detail['price']:>10.2f} | {(product_detail['price'] * product_detail['quantity']):>10.2f} |")
        print("+-----------------+------------+------------+------------+")



    print(f"|                                 Sub Total | {subt:>10.2f} |")
    print(f"|                                  Discount | {disc:>10.2f} |")
    print(f"|                                VAT @ 17.5 | {vat:>10.2f} |")
    print(f"+-------------------------------------------+------------+")   
    print(f"|                                Bill Total | {bill_total:>10.2f} |")
    print(f"+--------------------------------------------------------+")   
    print(f"|    THIS IS NOT A RECEIPT, KINDLY PAY N{bill_total:.2f}          |")
    print(f"+--------------------------------------------------------+")


def print_receipt(cart):
    os.system("clear")
    print(header_info)
    print("+-----------------+------------+------------+------------+")
    print("|       ITEM      |    QTY     |    PRICE   | TOTAL(NGN) |")
    print("+-----------------+------------+------------+------------+")

    for product_detail in cart:
        print(f"| {product_detail['product']:<15} | {product_detail['quantity']:>10} | {product_detail['price']:>10.2f} | {(product_detail['price'] * product_detail['quantity']):>10.2f} |")
        print("+-----------------+------------+------------+------------+")
        
    print(f"|                                 Sub Total | {subt:>10.2f} |")
    print(f"|                                  Discount | {disc:>10.2f} |")
    print(f"|                                VAT @ 17.5 | {vat:>10.2f} |")
    print(f"+-------------------------------------------+------------+")    
    print(f"|                                Bill Total | {bill_total:>10.2f} |")
    print(f"+--------------------------------------------------------+")    
    print(f"|                               VAT @ 17.5% | {bill_total:>10.2f} |"); 
    print(f"|                               Amount Paid | {amount_paid:>10.2f} |") 
    print(f"|                                   Balance | {amount_paid - bill_total:>10.2f} |")
    print(f"+--------------------------------------------------------+")
    print(f"|            THANK YOU FOR YOUR PATRONAGE                |")
    print(f"+--------------------------------------------------------+")



running = True

while running:
    product = input("What did the user buy? \n> ")
    quantity = int(input("How many pieces? \n> "))
    price = float(input("How much per unit? \n> "))

    cart = add_product_to(cart, product, quantity, price)

    terminate = input("Add more items? \n> ").lower()
    if terminate == 'yes':
        running = True
    else:
        running = False


cashier_name = input("What is your name? \n> ")
discount = int(input("How much discount will he/she get? \n> "))

header_info = f"""
SEMICOLON STORE
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, YABA, LAGOS.
TEL: 09876543213
Date: {datetime.now().strftime("%d-%b-%y %I:%M:%S %p")}
Cashier: {cashier_name}
Customer's Name: {customer_name}
"""

subt = sum(map(lambda product: product['price'] * product['quantity'], cart))
disc = subt * (discount / 100)
vat = subt * (17.5 / 100)
bill_total = subt + vat - disc


print_invoice(cart)
amount_paid = float(input("How much did the user give to you? \n> "))
print_receipt(cart)
