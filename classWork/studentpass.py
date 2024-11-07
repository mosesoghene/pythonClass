passes = 0
fails = 0

count = 1

while count <= 15:
    student_score = float(input(f"Enter student {count} score \n>  "))
    if student_score >= 0 and student_score <= 100:
        if student_score >=45:
            passes += 1
        else:
            fails += 1
    else:
        print("Score is out of range")
    
    count += 1

print(f"Total PASS: {passes}\nTotal FAILS: {fails}\n>  ")

