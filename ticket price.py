# this is the ticket price for each age

age = int(input("age: "))
student = int(input("type 1 if you are a student: "))
if age >= 13 and student == 1:
    print("$8")
else:
    if age >= 18:
        print("$12")
    elif age >= 13:
        print("$9")
    elif age >= 5:
        print("$7")
    else:
        print("free")