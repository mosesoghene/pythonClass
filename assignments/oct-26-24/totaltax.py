prompt = """
You are expected to enter 3 user names and their total earnings.
The required format is: Name earning separated by coma(,) i.e John 30000, Jane 25000, Leo 57000

Enter user details using the above details >> """

tax_data = input(prompt).split(", ")
print(tax_data)


