def get_switched_list(array, cut_off):
    if [type(array), type(cut_off)] == [list, int]:
        if len(array) == 0: raise IndexError
        cut_off = array.index(cut_off)
        return array[cut_off:] + array[:cut_off]
    raise TypeError


def get_split_list(array):
    if type(array) is list:
        if len(array) == 0: raise IndexError
        cut_off = len(array) // 2 if len(array) % 2 == 0 else len(array) // 2 + 1 
        return [array[:cut_off], array[cut_off:]]
    raise TypeError


def get_even_odds(array):
    if type(array) is list:
        if len(array) == 0: raise IndexError
        result = []
        for i in array: result.append(True) if (i % 2 == 0) else result.append(False)
        return result
    raise TypeError
    
print(get_switched_list([1,2,3,4,5], 2))
print(get_split_list([1,2,3,4,5]))
print(get_even_odds([1,2,3,4,5]))
