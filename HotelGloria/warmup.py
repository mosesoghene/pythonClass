import json
from pprint import pprint


def get_evens(text):
    return [int(i) for i in text if i.isdigit() and int(i) % 2 == 0]


def get_squares(number: int):
    if type(number) == int: return {1: number, 2: number ** 2}
    raise TypeError


def banana(numbers):
    if type(numbers) is list: return list(filter(lambda x: 20 <= x <= 50, numbers))
    raise TypeError


# print(banana([1, 2, 30, 4, 50]))

def get_grade(student_scores):
    student_grades = {}
    for key, value in student_scores.items():
        if value >= 90:
            student_grades[key] = "Oustanding"
        elif value >= 80:
            student_grades[key] = "Exceeds Expectations"
        elif value >= 70:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"

    return student_grades


scores = {"Gloria": 88, "Divine": 78, "Esther": 65, "Mercy": 75, "Uzo": 71}
# print(get_grade(scores))

records = {
    'class_1': {
        'students': [
            {"name": "Harry", 'scores': {'math': 88, 'English': 76}},
            {"name": "Solomon", 'scores': {'math': 95, 'English': 89}}
        ]
    },
    'class_2': {
        'students': [
            {"name": "Daniel", 'scores': {'math': 78, 'English': 72}},
            {'name': "Samuel", 'scores': {'math': 85, 'English': 80}}
        ]
    }
}


def get_student_average(data):
    averages = []
    for key, value in data.items():
        student_average = 0
        count = 0
        for student in value['students']:
            student_average += student['scores']['math']
            count += 1
        averages.append(student_average / count)
    return averages


database = {
    "usa": {"california": {"los angeles": 4000000, "san francisco": 8700000}},
    "canada": {"ontario": {"toronto": 2930000, "ottawa": 994837}}
}


def get_population(countries, country, state):
    if country not in countries.keys(): return f"wrong country input : {country}. Did you mean {tuple(countries.keys())}"
    if state not in countries[country].keys(): return f"wrong state input : {state}. Did you mean {tuple(countries[country].keys())}"
    population = ""
    for key, value in countries[country][state].items():
        population += f"{key.title()} : {value}\n"

    return population

def update_city_population(db, country, state, city, population):
    if country not in db: db[country] = {state:{city: population}}
    if state not in db[country]: db[country][state] = {city: population}
    else: db[country][state][city] = population
    return db

terminate = False
while not terminate:
    option = input("1. Get state populations \n2. Update a Country/State/City's population \n0. exit\n>> ")
    match option:
        case "1":
            country_input = input("Enter country: ").lower()
            state_input = input("Enter state: ").lower()
            print(get_population(database, country_input, state_input))
        case "2":
            country_input = input("Enter country: ").lower()
            state_input = input("Enter state: ").lower()
            city_input = input("Enter city: ").lower()
            population_input = int(input("Enter population (INPUT MUST BE INT TYPE: ...and a brain to use...): "))
            database = update_city_population(database, country_input, state_input, city_input, population_input)
            print(json.dumps(database, indent=4))
        case "0":
            terminate = True
            print("System shut down")
        case _:
            print("You have 2 arms, 2 hands, 2 legs, and a brain to use. Try again.")