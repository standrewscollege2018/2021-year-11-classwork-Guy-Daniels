# this program will show the recommended amount of tablets to takewhile

# this is to enter your age and weight

age = int(input("age: "))
weight = int(input("weight: "))

# this is the age constant

AGE_REQUIREMENT = 12

# this is to calculate the recommended dosage

if age <= 0 or weight <= 0:
    print("invalid")
else:
    if age >= AGE_REQUIREMENT:
        print("Take 2x500mg tablets")
    else:
        print("Recommended dosage is", weight *10)