# this program will make you guess a random number between 1 and 1000

import random
HIGH_SCORE = 1000000
keep_playing = True
while keep_playing == True:
    score = 0
    CORRECT_NUMBER = random.randint(1,1001)
    keep_guessing = True
    while keep_guessing == True:
        score += 1

        check_number = True:
            try:
                guess = int(input("Pick a number between 1-1000"))
                check_number = false
            except:
                print("Please print an integer")
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
            # printing out either lower, higher or within 5

            if number == CORRECT_NUMBER:
                keep_guessing = False

    print("Correct")

    if score < HIGH_SCORE:
        print("New high score is", score ,"!")
        HIGH_SCORE = score
    #


    play_again = input("Play again y/n: ")
    if play_again == "n":
        keep_playing = False
    elif play_again == "y":
        keep_playing = True
    else:
        keep_playing = False
        print("invalid answer")