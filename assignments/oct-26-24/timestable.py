table_number = int(input("Input the times table >> "))
table_length = int(input("Input the length of the table >> "))

for i in range(table_length):
    print(f"{table_number} X {i} = {table_length * i}")
    
