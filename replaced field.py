age = 24
print("my age is " + str(age) + " years")
# or
print("my age is {0} years".format(age))
# replace the fields
print("There are {0} days in , {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(31, "jan", "mar", "may", "july", "aug",
                                                                             "oct", "dec"))
# respective nb 0 to 7 total 8 items in the list. Actually 7 replacement field after the dot format
print("jan:{2}, feb: {0}, mar: {1}".format(28, 30, 31))
#  replaced string position
