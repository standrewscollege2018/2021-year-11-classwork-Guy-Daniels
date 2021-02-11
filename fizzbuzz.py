# this is fizzbuzz

number = int(input("Number: "))

import time
delay = 0.25

for i in range(1,number):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
    time.sleep(delay)