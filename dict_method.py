d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = "ten"
print(v)  # 10 added to dictionary

print()
print("ten" in v)
print("twenty" in v)

keys = list(d.keys())
values = list(v)  # => list(d.values())
if "ten" in values:  # looping to dict items
    index = values.index("ten")
    key = keys[index]
    print(f"{d[key]} was found with key {key}")
print()
for key, value in d.items():
    if value == "ten":
        print(f"{d[key]} was found with key {key}")
        

# Code for  the dict 'update' method
# d2 = {
#    8: "lucky for eight",
#  10: "ten",
#   3: "this is the new three",
# }

# d.update(d2)
# for key, value in d.items():
#    print(key, value)

# Code for  the remaining dict method
# **************************************
# new_dict = dict.fromkeys(pantry_items, 0) # dict : class , fromkeys: passing iterable
# print(new_dict)

# keys = d.keys()  # a list containing all dictionary keys
# print(keys)

# for item in d.keys():
#    print(item)  # iterating over a dictionary
