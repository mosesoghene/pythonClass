def is_palindrome(text):
    dummy = ""
    for i in range(len(text) - 1, -1, -1):
        dummy += text[i]
    
    return True if dummy == text else False
    
print(is_palindrome("hello"))
