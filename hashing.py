data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit "),
    ("grape", "a small, sweet fruit growing in bunche "),
    ("melon", "sweet and juicy")
]


# ord function converted character into number
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))
# every character represented by a number

def simple_hash(s: str) -> int:
    """ A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10  # use remainder operator


# for key, value in data:
#    h = simple_hash(key)
#    print(key, h)
keys = [""] * 10  # hold the value 10 items
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(Key)
    print(key, h)
    keys[h] = key
    values[h] = value
print(keys)
print(values)
