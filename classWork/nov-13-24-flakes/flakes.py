import re

def is_int(value): return bool(re.match(r"^\d+$", str(value)))
    
def is_valid_number(value): return bool(re.match(r"^\d+(\.\d+)?$", str(value)))

def is_float(value): return bool(re.match(r"^\d+(\.\d+)$", str(value)))


def divide_or_square(number):    
    if is_int(number):
        number = int(number)
        if number % 5 == 0:
            return round(number ** 0.5, 2)
        else:
            return number % 5
    
    raise TypeError


def get_future_inv(investment_amount, monthly_interest_rate, years):
    if is_int(years) \
        and is_valid_number(investment_amount) \
        and is_valid_number(monthly_interest_rate):
        
        investment_amount = float(investment_amount)
        monthly_interest_rate = float(monthly_interest_rate)
        number_of_months = int(years) * 12
        
        future_investment_amount = investment_amount * (1 + (monthly_interest_rate/100)) ** number_of_months
        return round(future_investment_amount, 2)
        
    raise TypeError


def only_floats(data_one, data_two):
    if not is_valid_number(data_one) or not is_valid_number(data_one):
        raise TypeError 
        
    return 2 if is_float(data_one) and is_float(data_two) else 1 if is_float(data_one) or is_float(data_two) else 0


def my_discount(price, discount):
    if is_valid_number(price) and is_valid_number(discount):
        price, discount = float(price), float(discount)
        
        return price - price * (discount / 100)
        
    raise TypeError
    
