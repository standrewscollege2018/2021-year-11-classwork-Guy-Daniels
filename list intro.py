# this program demonstrates how lists work

# For lists, we use square brackets
# Items in lists are seperated by commas
# String needs to have speech marks around it
names = ["Max", "Noah"]

# To print a list
print(names)

# To print an individual item from a list, we use
# it's index (position from the list)
print(names[0])

# To add something to the end of a list, we use append()
names.append("Neko")
print(names)

# To add something to a specific position, use insert()
names.insert(1, "Dr Evil")
print(names)

# Lists are mutable (changeable)
# To change the value of an item in a list, we just
# over-write it
names[1] = "Dr Good"
print(names)

# len(list) returns the number of items in a list
print(len(names))

# There are two ways we can loop through a list to
# print out the items

# 1. a simple loop with no range
for n in names:
    print(n)

# 2. Use range() to get a numbered list
# Use len(list) to get how many times to loop
for i in range(len(names)):
    print(i+1, names[i])