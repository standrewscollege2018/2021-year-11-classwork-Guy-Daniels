#

print("Welcome to my raffle")
prize = input("What is the prize: ")

import random
names = []

keep_asking = True

while keep_asking == True:
    name = input("Enter a name: ")
    if name == "end":
        keep_asking = False
    else:
        names.append(name)

contestant_number = len(names)
random_number = random.randint(0,contestant_number)

print(names[random_number-1])
print("You won", prize)