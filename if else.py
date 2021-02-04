# this program is learning how to use the if else command


# this is where they enter the score variable
score = int(input("Score: "))

# this is what will be printed depending on the score

if score > 100:
    print("invalid")
elif score >= 90:
    print("Excellence")
elif score >= 70:
    print("Merit")
elif score >= 50:
    print("Achieved")
elif score < 0:
    print("invalid")
else:
    print("Not achieved")