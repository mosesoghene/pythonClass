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
