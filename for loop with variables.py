# this program counts numbers up in the entered values
# this is where the variables are entered
start = int(input("Start number: "))
end = int(input("End number: "))
step = int(input("Step: "))

import time
delay = 1
# print the numbers
for num in range(start,end,step):
    print(num)
    time.sleep(delay)