# 3.2 Returning Values

import math

def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
except ValueError:
    print("Oh no! That's not a valid value. Try again...")
#except ZeroDivisionError:
    # TODO: write exception handling
else:
    amount_due = split_check(total_due, number_of_people)
    print("Each person owes ${}".format(amount_due))
