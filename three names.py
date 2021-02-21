# this programs asks for three names and enters them into a list and prints it

# names list will store the entered names
names = []

# now we loop 3 times, asking for names and appending them
for i in range(3):
    name = input("Enter a name: ")
    names.append(name)

# this prints out the list
for n in names:
    print(n)