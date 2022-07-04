animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

things = animals.copy()  # now two separate dictionary ,modify the animals dictionary
animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])
# immutable values it makes no difference whether copy is shallow or deep.
# where it becomes important is mutable values in the dictionary .
