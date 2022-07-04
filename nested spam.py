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

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))



