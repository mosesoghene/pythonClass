def sum_of_even(data):
    if type(data) in [list]:
        return sum([number for number in data if number % 2 == 0])    
    raise TypeError


def vowel_count_of(data):
    if type(data) in [str]:
        return len([letter for letter in data if letter.lower() in "aeiou"])
    raise TypeError


def is_anagram(data, check):
    if type(data) == str and type(check) == str:
        for letter in data: 
            if letter not in check: return False
        return True
    raise TypeError


def is_prime(data):
    if type(data) == int:
        for number in range(2, data): 
            if data % number == 0: return False
        return True
    raise TypeError


def is_palindrom(data):
    if type(data) == str:
        check = data[::-1]
        return True if data == check else False
    raise TypeError


def average(data):
    if type(data) is list:
        total = sum(data)
        result = total / len(data)
        return result
    raise TypeError

def reverse_string(data):
    if type(data) is str: return data[::-1]
    raise TypeError


def capitalise_list(data):
    if type(data) is list: return [item.capitalize() for item in data]
    raise TypeError


def contains_duplicate(data):
    if type(data) is list: return True if len(set(data)) < len(data) else False
    raise TypeError

def remove_spaces(data):
    if type(data) is str: return data.replace(" ", "")
    raise TypeError

def get_intersect(data, check):
    if type(data) is list and type(check) is list:
        data = set(data)
        intersect = data.intersection(check)
        if len(intersect) > 1:
            return list(intersect)
        return list(intersect)[0]
    raise TypeError
    
    
def sorted_by_len_of_string(data):
    if type(data) is list: return sorted(data, key=len, reverse=False)
    raise TypeError


def factorial(number):
    if type(number) is int:
        factorial = 1
        for i in range(number, 0, -1):
            factorial *= i
        return factorial
    raise TypeError
    

def sum_of_digits(data):
    if type(data) in [int, str]:
        result = 0
        for i in str(data):
            result += int(i)
        return result
    raise TypeError

def sum_of_odd_digits(data):
    if type(data) in [int, str]:
        result = 0
        for i in str(data):
            if int(i) % 2 != 0:
                result += int(i)
        return result
    raise TypeError
 


def get_acronym(data):
    if type(data) is str:
        acronym = ""
        for word in data.split(" "): acronym += word[0]        
        return acronym
    raise TypeError

def sum_of_product(data):
    if type(data) is list:
        total = 0
        for num in data: total += sum(data) - num
        return total
    raise TypeError

 
def merge_and_sort(data, data2):
    if type(data) is list and type(data2) is list:
        data += data2
        data.sort()
        return data
    raise TypeError
