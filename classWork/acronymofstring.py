def string_acronym(string):
    acronym = ""
    string = string.split(" ")
    for text in string:
        acronym += text[0]
    
    return acronym.upper()

print(string_acronym("Portable Network Graphics"))
    
