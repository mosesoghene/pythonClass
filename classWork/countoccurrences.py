def count_occurrences(char, string):
    count = 0
    for letter in string:
        if char == letter:
            count += 1
            
    return count

print(count_occurrences('e', "elephant"))
