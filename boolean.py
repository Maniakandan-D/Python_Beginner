if 0:  # o is consider false
    print("True")
else:
    print("False")
name = input("Please enter your name: ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")  # empty string also consider false
