def is_even(number):
    return True if type(number) in [int, float] and number % 2 == 0 else False


def sum_even_of(array):
    if type(array) is list:
        total = 0
        for num in array:
            if is_even(num): total += num
        return total
    raise TypeError

def sum_odds_of(array):
    if type(array) is list:
        total = 0
        for num in array:
            if not is_even(num): total += num
        return total
    raise TypeError


def is_prime(number):
    if number <=1: return False
    if number == 2: return True
    
    for i in range(2, number):
        if number % i == 0: 
            return False        
    return True
    
def get_primes_of(number):
    if type(number) is int: return [i for i in range(1, number) if is_prime(i)]


def get_numbers_in_range_of(number):
    if type(number) is int:
        return [i for i in range(1,number)]
    raise TypeError


def get_cube_root(numbers: list):
    if type(numbers) in [list, tuple, set]: 
        return [
            round(element ** (1/3), 5) \
            for element in numbers \
            if type(element) in [int, float]
            ]
    else: raise TypeError


def count_even(array):
    if type(array) in [list, tuple, set]: return len([i for i in array if (i % 2 == 0) ])
    else: raise TypeError
    


