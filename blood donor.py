# this program is to check whether you are old enough and weigh enough to donate blood

BLOOD_AGE = 16
BLOOD_WEIGHT = 50

age = int(input("Age: "))
weight = int(input("Weight: "))

if age >= BLOOD_AGE and weight >= BLOOD_WEIGHT:
    print("You are eligible")
else:
    print("You are not eligible")