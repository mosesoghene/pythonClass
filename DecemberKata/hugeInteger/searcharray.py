def search_array(arr, target) -> [int, str]:
    if target in arr:
        return arr.index(target)
    return "Not Available"


def count_positive_negative_of(arr):
    positive_count = len([i for i in arr if i > 0])
    negative_count = len([i for i in arr if i < 0])
    zeros_count = len([i for i in arr if i == 0])
    return positive_count, negative_count, zeros_count

