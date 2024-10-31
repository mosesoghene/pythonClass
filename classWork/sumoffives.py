numbers = input("Enter a number to get the sum \n> ")


def sum_of_numbers(array):
    total = 0
    step = 0
    while step < (len(array)):
        if array[step].isdigit():
            if int(array[step]) >= 5:
                total += 1
                step += 1
            else:
                total += 0
                step += 1
        else:
            print(f"'{array[step]}' is not a digit")
            step += 1
    else:
        print(f"\nTotal: {total}")


sum_of_numbers(numbers)
