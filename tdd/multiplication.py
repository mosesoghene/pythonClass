import re

def is_int(value):
    return bool(re.match(r"^-?\d+$", value))
    
def is_float(value):
    return bool(re.match(r"^-?\d+(\.\d+)$", value))
    
def is_negative_value(value):
    return bool(re.match(r"^-\d+(\.\d+)?$", value))


def multiplication(base, multiple):
    base = str(base)
    multiple = str(multiple)
    result = 0
    
    if is_negative_value(base) and is_negative_value(multiple): 
        if is_float(multiple) and is_int(base):
            multiple = float(multiple)
            base = abs(int(base))
            
            for number in range(base):
                result += multiple    
    
            return abs(round(result, 0))
            
        elif is_int(multiple) and is_float(base):
            multiple = abs(int(multiple))
            base = abs(float(base))
            
            for number in range(multiple):
                result += base    
    
            return round(result, 0)
            
        elif is_int(multiple) and is_int(base):
            multiple = abs(int(multiple))
            base = abs(int(base))
            
            for number in range(multiple):
                result += base   
    
            return round(result, 0)
            
        elif is_float(multiple) and is_float(base):
            multiple = round(float(multiple), 0)
            base = round(float(base), 0)
            
            for i in range(base):
                result += multiple
            
            return round(abs(result))
                
    elif not (is_negative_value(base)) and  not (is_negative_value(multiple)):
        if is_float(multiple) and is_int(base):
            multiple = float(multiple)
            base = int(base)
            
            for number in range(base):
                result += multiple    
    
            return round(result)
            
        elif is_int(multiple) and is_float(base):
            multiple = int(multiple)
            base = float(base)
            
            for number in range(multiple):
                result += base    
    
            return round(result)
            
        elif is_int(multiple) and is_int(base):
            multiple = int(multiple)
            base = int(base)
            
            for number in range(multiple):
                result += base   
    
            return round(result)
            
        elif is_float(multiple) and is_float(base):
            multiple = round(float(multiple), 0)
            base = round(float(base), 0)
            
            for i in range(base):
                result += multiple
            
            return round(result)
            
    elif is_negative_value(base) and not (is_negative_value(multiple)):
        if is_float(multiple) and is_int(base):
            multiple = float(multiple)
            base = int(base)
            
            for number in range(base):
                result += base    
    
            return round(result)
            
        elif is_int(multiple) and is_float(base):
            multiple = int(multiple)
            base = float(base)
            
            for number in range(multiple):
                result += base    
    
            return round(result)
            
        elif is_int(multiple) and is_int(base):
            multiple = int(multiple)
            base = int(base)
            
            for number in range(multiple):
                result += base   
    
            return round(result)
            
        elif is_float(multiple) and is_float(base):
            multiple = round(float(multiple), 0)
            base = round(float(base), 0)
            
            for i in range(base):
                result += multiple
            
            return round(result)
    elif not is_negative_value(base) and is_negative_value(multiple):
        if is_float(multiple) and is_int(base):
            multiple = float(multiple)
            base = int(base)
            
            for number in range(base):
                result += nultiple    
    
            return round(result)
            
        elif is_int(multiple) and is_float(base):
            multiple = int(multiple)
            base = float(base)
            
            for number in range(multiple):
                result += base    
    
            return round(result)
            
        elif is_int(multiple) and is_int(base):
            multiple = int(multiple)
            base = int(base)
            
            for number in range(base):
                result += multiple   
    
            return round(result)
            
        elif is_float(multiple) and is_float(base):
            multiple = round(float(multiple), 0)
            base = round(float(base), 0)
            
            for i in range(base):
                result += multiple
            
            return round(result)
    raise TypeError
    
    
