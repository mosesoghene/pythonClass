days = int(input("Enter amount of days \n> "))
RUPIE = 1
total = 0
if days <= 5:
    total = 0.5 * RUPIE
elif days > 5 < 10:
    total = (days - 5) * RUPIE
elif days >= 30:
    print("You are banned!!!")

print(f"You are to pay the library ₹{total} in total.")
