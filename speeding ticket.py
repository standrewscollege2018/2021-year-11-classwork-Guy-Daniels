# this program tells you how much you should be fined
# depending on how much over the speed limit you were
criminals = ["Josh McPhail", "Tom Kerry", "Mitchell Corkery"]
statement = []
keep_asking = True
asking_for_speed = True
while keep_asking == True:
    name = input("Name: ")
    if name in (criminals):
        print("You are under arrest")
    elif name == "end":
        keep_asking = False
    else:
        while asking_for_speed == True:
            try:
                limit = int(input("What is the speed limit: "))
                asking_for_speed = False
            except:
                print("Invalid answer")
            speed = int(input("What speed were you at: "))
            if speed < limit+1:
                added_statement = (name, "Have a nice day")
            else:
                amount_over = speed-limit
                if amount_over < 11:
                    fine = 30
                elif amount_over < 21:
                    fine = 80
                elif amount_over <= 29:
                    fine = 130
                elif amount_over >= 30:
                    fine = 180
                else:
                    print("Error")
                added_statement = (name, "You are fined", fine)
            statement.append(added_statement)

print(statement)