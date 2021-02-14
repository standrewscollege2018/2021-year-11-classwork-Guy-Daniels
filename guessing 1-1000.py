#

import random

CORRECT_NUMBER = random.randint(1,1000)

keep_guessing = True

while keep_guessing == True:
    number = int(input("Guess a number between 1 and 1000: "))
    if number <= 0 or number >= 1001:
        print("invalid")
    else:
        if number == CORRECT_NUMBER:
            keep_guessing = False
        elif abs(CORRECT_NUMBER - number) <= 5:
            print("within 5")
        elif number > CORRECT_NUMBER:
            print("Lower")
        elif number < CORRECT_NUMBER:
            print("Higher")

        if number == CORRECT_NUMBER:
            keep_guessing = False


print("Correct")

