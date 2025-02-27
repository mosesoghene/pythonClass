from operator import countOf
from collections import Counter


def frequency_of(string: str) -> dict:
    if type(string) is not str: raise TypeError("String must be of type 'str' ")
    if len(string) == 0: raise ValueError("String cannot be empty")
    return Counter(string)

def swapchars(string: str) -> str:
    if type(string) != str: raise TypeError("String must be of type 'str' ")
    string = string.replace(" ", "").split(",")
    return f"{string[1][:2] + string[0][2:]} {string[0][:2] + string[1][2:]}"

def insert_into(string: str, text: str):
    if type(string) != str or type(text) != str: raise TypeError("Value must be string")
    string = list(string)
    if len(string) % 2 == 0: string.insert(len(string) // 2, text)
    else: string.append(text)
    return "".join(string)

def arrange_word(word: str) -> str:
    if type(word) != str: raise TypeError("Value must be string")
    upper = list(filter(lambda c: c.isupper(), word))
    lower = list(filter(lambda c: c.islower(), word))
    return "".join(upper) + "".join(lower)


def count_of(word, char):
    if type(word) != str or type(char) != str: raise TypeError("Values must be string")
    return f"{char}", countOf(word, char)

def remove_special_chars(string: str) -> str:
    if type(string) != str: raise TypeError("String must be of type 'str' ")
    return "".join(filter(lambda char: char.isalpha(), string))