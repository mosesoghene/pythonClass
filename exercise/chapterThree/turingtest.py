question = input("what is your problem?  ")
next_question = input("have you had this problem before (yes or no)?  ")

if next_question.lower() == "yes":
    print("well, you have it again.")
elif next_question.lower() == "no":
    print("well, you have it now")
