data_one = 1024
data_one_check = 4

data_two = 10
data_two_check = 2

if data_one % data_one_check == 0:
    print(f"{data_one} is a multiple of {data_one_check}s")
else:
    print(f"{data_one} is not a multiple of {data_one_check}s")
    
if data_two % data_two_check == 0:
    print(f"{data_two} is a multiple of {data_two_check}s")
else:
    print(f"{data_two} is not a multiple of {data_two_check}s")
