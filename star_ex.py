numbers = (1, 2, 3, 4, 5)

print(numbers, sep=";")
print(*numbers, sep=";")  # '*numbers' was unpacked then the unpacked values passed to the print function
print(1, 2, 3, 4, 5, sep=";")  # individual values passed print function


def test_star(*args): # inside of tuple args is a tuple
    print(args)
    for x in args:
        print(x)


test_star(1, 2, 3, 4, 5)

print()
test_star()
