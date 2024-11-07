data = int(input("Enter number to check if prime: \n>  "))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

print(is_prime(data) )



data = int(input("Enter number to get even range: \n>  "))

def number_of_even(number):
    return len(list(range(2, number+1, 2)))

print("Total even numbers are: ", number_of_even(data))
