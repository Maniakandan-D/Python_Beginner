menu = [
    ["eggs", "bread"],
    ["eggs", "noodles", "masala"],
    ["eggs", "tomato", "onion", "noodles", "rice"],
    ["tomato", "onion", "spam"],
    ["spam", "tomato", "onion", "spam", "noodles", "rice", "masala", "spam"],
    ["spam", "tomato", "onion", "spam"],
    ["spam", "eggs", "tomato", "spam", "onion", "spam", "noodles", "rice", "spam"],
    ["eggs", "tomato", "onion", "noodles", "rice", "masala", "bread"]
]
# for meal in menu:
#    for index in range(len(meal) - 1, - 1, - 1):
#        if meal[index] == "spam":
#            del meal[index]
#
#    print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)

    print()
