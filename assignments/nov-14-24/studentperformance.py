from os import system

student_names = []
student_scores = {
    'python': [],
    'java': [],
    'datascience': [],
    'designthinking': []
}

LIMIT = 2
count = 0

system('clear')
while count < LIMIT:
    name = input(f"Enter name for student[{count+1}]:\n> ")
    student_names.append(name)
    keys = list(student_scores.keys())
    i = 0
    for key in keys:
        try:
            score = int(input(f"Enter student[{count+1}]'s score for {key.upper()}:\n> "))
            if score > 0 and score <= 100:
                student_scores[key].append(score)
                i += 1
            else:
                i -= 1
                keys.insert(i, key)
        except:        
            print("Value out of range 1 - 100")
        
    else:
        i = 0        
        system('clear')
            
            
    count += 1


def get_top_scorer(student_info, course):
    return f"{course.capitalize()}: {student_info[0][student_info[1][course].index(max(student_info[1][course]))]} came top scoring {max(student_info[1][course])}%"

def get_least_scorer(student_info, course):
    return f"{course.capitalize()}: {student_info[0][student_info[1][course].index(min(student_info[1][course]))]} came least scoring {min(student_info[1][course])}%\n"

system("clear")
student_info = [student_names, student_scores]

print(get_top_scorer(student_info, 'python'))
print(get_least_scorer(student_info, 'python'))

print(get_top_scorer(student_info, 'java'))
print(get_least_scorer(student_info, 'java'))

print(get_top_scorer(student_info, 'datascience'))
print(get_least_scorer(student_info, 'datascience'))

print(get_top_scorer(student_info, 'designthinking'))
print(get_least_scorer(student_info, 'designthinking'))
