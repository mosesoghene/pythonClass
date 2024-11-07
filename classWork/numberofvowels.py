import re

def number_of_vowels(text):
    count = 0
    for letter in text:
        if bool(re.match(r"^[aeiou]$", letter)):
            count += 1
    
    return count

print(number_of_vowels("python is sweet"))
