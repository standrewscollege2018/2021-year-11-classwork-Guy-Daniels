#

# set boolean to true
keep_asking = True

# start asking their name
while keep_asking == True:
    name = input("Enter your name: ")
    if name == "Guy":
        keep_asking = False
    else:
        print("Wrong name")

# loop is now finished, so greet Guy
print("Hi Guy")