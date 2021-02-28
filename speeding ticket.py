# this program tells you how much you should be fined
# depending on how much over the speed limit you were
criminals = ["Josh McPhail", "Tom Kerry", "Mitchell Corkery"]
keep_asking = True
while keep_asking == True:
    name = input("Name: ")
    if name in (criminals):
        print("You are under arrest")
    else:
        limit = int(input("What is the speed limit: "))
        speed = int(input("What speed were you at: "))
        if speed < limit+1:
            print("Have a nice day")
        else:
            amount_over = speed-limit
            if amount_over < 10:
                print(name, "")