# up to not including
parrot = "Norwegian Blue"
print(parrot[0:6])
print(parrot[0:3])
print(parrot[10:14])
print(parrot[:9])
print(parrot[10:])
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + (parrot[6:]))
print(parrot[:])
print()
# use a step in slicing
print(parrot[0:6:3])
print(parrot[0:6:2])
print(parrot[2:6:4])
# use slicing
number = "9,123;234:43 98,12"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val)for val in values])
