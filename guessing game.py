#

CORRECT_NUMBER = 3

keep_guessing = True

while keep_guessing == True:
    number = int(input("Guess a number between 1 and 10: "))
    if number <= 0 or number >= 11:
        print("invalid")
    else:
        if number == CORRECT_NUMBER:
            keep_guessing = False
        else:
            print("Wrong number")

print("Correct")