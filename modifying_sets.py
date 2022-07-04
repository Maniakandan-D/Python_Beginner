numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

while len(numbers) < 4:
    value = int(input("Please enter the next value: "))
    numbers.add(value)
print(numbers)
