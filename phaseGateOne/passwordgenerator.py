from random import choice
import string

def password_generator():
    uppercase_letters = [letter for letter in string.ascii_uppercase]
    lowercase_letters = [letter for letter in string.ascii_lowercase]    
    punctuations_letters = [punctuation for punctuation in string.punctuation]
    digits_letters = [digit for digit in string.digits]
    
    generated_password = ""
    for _ in range(4):
        generated_password += choice(uppercase_letters)
        generated_password += choice(lowercase_letters)
        generated_password += choice(punctuations_letters)
        generated_password += choice(digits_letters)
    
    return generated_password
    
    
