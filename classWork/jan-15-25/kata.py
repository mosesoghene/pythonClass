def get_even_odd_count(array):    
    return [len(list(filter(lambda x: x % 2 != 0, array))), len(list(filter(lambda x: x % 2 == 0, array)))]


data1 = [1,2,3,6,8,10,1]
data2 = [5,3,7,9,2,8]
print(get_even_odd_count(data1))
print(get_even_odd_count(data2))
