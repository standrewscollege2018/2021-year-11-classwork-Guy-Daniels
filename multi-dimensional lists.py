# this program demonstrates lists inside lists
# called multi-dimentional arrays
person = []
people = [["Dr Evil", 45], ["Gru", 34], ["Emperor", 200]]

amount_of_names = len(people)

# to print a sub-list:
print(people[0])

name = input("Enter a name: ")
age = input("Enter an age: ")

person.append(name)
person.append(age)

people.append(person)

# To print items in a sub-list:
for i in range(0,amount_of_names):
    print("{} is {} years old".format(people[i][0], people[i][1]))