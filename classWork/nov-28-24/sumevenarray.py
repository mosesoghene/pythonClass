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
    raise TypeError
    

def true_false_even_odds(array):
    if type(array) in [list, tuple, set]: return [True  if (i % 2 == 0) else False for i in array ]
    raise TypeError

def capitalize_(array):
    if type(array) in [list, tuple, set]: return [i.lower().capitalize() for i in array ]
    raise TypeError

def func_():
    return [i for i in range(3, 31) if i % 3 == 0 ]

def square_odds(array):
    return [i**2 for i in array if i % 2 != 0 ]
    

def squares(number):
    return list(map(lambda x: x * x, range(1, number+1)))

def all_greater_than_ten(numbers):
    if type(numbers) in [list, tuple, set]: return list(filter(lambda x: x > 10, numbers))
    raise ValueError
    
def is_list_palindrome(array):
    return list(map(lambda x: str(x) == str(x)[::-1], array))


def sum_of(number):
    return sum(map(lambda x: int(x), str(192374)))

# list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), "1a2b3c")))
# ['madam', 'apple', 'racecar']
print(all_greater_than_ten([1,5,12,15,8]) )


def strip_vowels_in(array):
    if type(array) is list:
        return ["".join(filter(lambda x: x.lower() not in "aeiou", word )) for word in array]

def pay_even_dict(number):
    return {x: x ** 2 for x in range(1,number+1) if (x ** 2) % 2 == 0}


print(strip_vowels_in(['Orange', 'apple', 'ice', 'Beans', 'Rice']))
