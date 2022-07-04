activity = input("What would you like to do Today? ")

if "college" not in activity.casefold():  # convert lowercase
    print("but i want to go the college")  # string comparison are case sensitive
