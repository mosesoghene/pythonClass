def max_number(numbers):
    if type(numbers) == list:
        if len(numbers) == 0: raise IndexError    
        largest = numbers[0]
        for number in numbers:
            if type(number) in [int, float] and number > largest:
                largest = number
        return largest
    raise TypeError


def reverse_list(array):
    if type(array) is list:
        if len(array) == 0: raise IndexError
        return array[::-1]
    raise TypeError

def value_in(value, array):
    if type(array) is list:
        if len(array) == 0: raise IndexError
        return True if value in array else False
    raise TypeError

def get_odd_elements(array):
    if type(array) is list:
        if len(array) == 0: raise IndexError
        return [array[i] for i in range(0, len(array), 2) ]
    raise TypeError

def get_even_elements(array):
    if type(array) is list:
        if len(array) == 0: raise IndexError
        return [array[i] for i in range(1, len(array), 2) ]
    raise TypeError
    
def get_running_sum(array):
    if type(array) is list:        
        if len(array) == 0: raise IndexError
        total = 0
        for i in array: 
            if type(i) in [int, float]: total += i
        return total
    raise TypeError

def is_palindrome(string):
    if type(string) is str:        
        if len(string) == 0: raise IndexError
        return True if string == str(string[::-1]) else False
    raise TypeError

def join_list(array_a, array_b):
    if [type(array_a),type(array_a)]  == [list, list]:
        return array_a + array_b
    raise TypeError
    
def alternate_list(array_a, array_b):
    if [type(array_a),type(array_a)]  == [list, list]:
        result = []
        for i in range(max([len(array_a), len(array_b)])):
            if i < len(array_a): result.append(array_a[i])
            if i < len(array_b): result.append(array_b[i])
        return result
    raise TypeError

def list_of(number):
    if type(number) is int:
        result = [int(i) for i in str(number)]        
        return result
    raise TypeError
    
def is_even(number):
    if type(number) is int:
        result = True if number % 2 == 0 else False       
        return result
    raise TypeError

def is_prime(number):
    if type(number) is int:
        if number <= 1: return False
        for i in range(2, number):
            if number % i == 0: return False
        return True
    raise TypeError

def subtract(x, y):
    if [type(x), type(y)] == [int, int]: return abs(x - y)
    raise TypeError

def divide(x, y):
    try: 
        return x / y if y != 0 else 0
    except TypeError:
        raise TypeError

def factor_of(number):
    try:
        factors = 0
        for i in range(1, number+1):
            if number % i == 0: factors += 1
        return factors
    except TypeError:
        raise TypeError

def is_square(number):
    try:
        from math import sqrt
        return True if (int(sqrt(number)) ** 2) == number else False
    except TypeError:
        raise TypeError

def is_int_palindrome(number):
    if type(number) is int:
        return True if str(number) == str(number)[::-1] else False
    raise TypeError


def factorial_of(number):
    if type(number) is int:
        factorial =  1
        for i in range(number, 0, -1): factorial *= i
        return factorial
    raise TypeError

def square_of(number):
    if type(number) in [int, float]: return number * number
    raise TypeError

