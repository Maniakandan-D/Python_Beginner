name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Hi {} Welcome, to holiday".format(name))
else:
    print("Sorry, {} you come after {} years".format(name, 18 - age))
