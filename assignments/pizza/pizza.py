menu = """
+-----+-------------+--------------------+---------------+
| S/N | Pizza Type  | Number of Slices   | Price Per Box |
+-----+-------------+--------------------+---------------+
| 1.  | Sapa size   |  4                 | 2,500         |
+-----+-------------+--------------------+---------------+
| 2.  | Small money |  6                 | 2,900         |
+-----+-------------+--------------------+---------------+
| 3.  | Big Boys    |  8                 | 4,000         |
+-----+-------------+--------------------+---------------+
| 4.  | Odogwu      |  12                | 5,200         |
+-----+-------------+--------------------+---------------+
"""

SLICES_DB = {1:4, 2:6, 3:8, 4:12}
PRICE_DB = {1: 2500, 2: 2900, 3: 4000, 4: 5200}
PIZZA_TYPES = {1: "SAPA", 2: "SMALL MONEY", 3: "BG BOYS", 4: "ODOGWU"}


def get_guest_number(user_input): 
    if type(user_input) is int and user_input > 0:
        return int(user_input)
    raise ValueError

def get_pizza_type(user_input):
    if user_input is int: return int(user_input)
    raise ValueError


def calculate_n_of_box(pizza_type, n_of_guests):
    return n_of_guests // slices_db[pizza_type]
    

def calculate_price(pizza_type, prices_db, n_of_boxes):
    return n_of_boxes * prices_db[pizza_type]

def get_remaining_slices(n_of_guests, pizza_type, slices_db):
    return n_of_guests % slices_db[pizza_type]
    

app_running = True
while app_running:
    print(menu)
    
    pizza_type_input = input("Enter pizza type \n> ")
    guest_n_input = input("Enter number of guests \n> ")
    
    pizza_type = get_pizza_type(pizza_type_input)
    guests_number = get_guest_number(guest_n_input)
    
    boxes_count = calculate_n_of_box(pizza_type, guests_number)
    price = calculate_price(pizza_type, PRICE_DB, boxes_coun)
    remainder = get_remaining_slices(guests_number, pizza_type, SLICES_DB)
    
    print(f"""Total Boxes: {boxes_count} {"boxes" if boxes_count > 1 else "box"}
    Total Guests: {guests_number}
    Pizza Type: {PIZZA_TYPE[pizza_type]}
    Total Price: {price:.2f} (ngn)
    Remaining slices: {remainder} slice(s) will remain
    """)
    
    checkpoint = input("1. Start another order \n2. Exit program \n> ")
    if checkpoint.isdigit():
        match int(checkpoint):
            case 1:
                continue
            case 2:
                print("THANK YOU FOR YOUR ORDER!!!")
                app_running = False
            case _ :
                print("You should be jailed, you had only 2 options to pick from and {checkpoint} isn't")

