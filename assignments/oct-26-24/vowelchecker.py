user_input = input("Input an alphabet >> ").lower()
vowels = "aeiou"

if user_input.isalpha():
    if len(user_input) == 1:
        if user_input in vowels:
            print("Input letter is a vowel")
        else:
            print("input letter is a consonant")
    else:
        print(f"'{user_input}' is more than one letter. Expected 1 alphabet letter")
else:
    print(f"'{user_input}' contains a non-alpahbet letter")

