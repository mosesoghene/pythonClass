def remove_char(text, char):
    text = [letter for letter in text if letter not in char]    
    return "".join(text)
    
print(remove_char("Food", "o"))
