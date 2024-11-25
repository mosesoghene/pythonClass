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
