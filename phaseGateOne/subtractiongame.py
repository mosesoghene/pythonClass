"""
set score = 0
set total_questions = 10
set current_questions = 1
record the current time: datetime.date.now()
while current_questions <= total questions
    generate minuend between 40 - 100
    generate subtrahend between 0 - 40 ( this will make sure subtrahend is always smaller and result is always positive)
    prompt user to enter answer with correct question
    check if user_input is a valid digit(str.isdgit() method) and input == minuend - subtrahend
        if check is true, increase score by 1
    increase current_question by 1
record current time at the end of while loop
calculate time in seconds
print score and time


"""

from datetime import datetime
from random import randint


score = 0
TOTAL_QUESTION_NUMBERS = 10
current_question_number = 1

start_time = datetime.now()
while current_question_number <=TOTAL_QUESTION_NUMBERS:
    minuend = randint(40, 100)
    subtrahend = randint(0,40)
    user_answer = input(f"Question {current_question_number}: What is {minuend} - {subtrahend}? \n> ")
    if user_answer.isdigit() and int(user_answer) == (minuend - subtrahend):
        score += 1
    
    current_question_number += 1

end_time = datetime.now()
total_time = str(end_time - start_time).split(":")
hour = int(total_time[0]);  minute = int(total_time[1]);  seconds = float(total_time[2])

if hour > 0: hour * 60 * 60
if minute > 0: minute * 60

total_seconds = hour + minute + round(seconds)

print(f"Total Score: {score} {'points' if score > 1 else 'point'} \nTotal Time: {total_seconds} seconds")
            
