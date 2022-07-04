# Find Maximum Number
numbers = [30, 67, 54, 7, 8, 11]
max = numbers[0]
# max= find_max(numbers)
for numbers in numbers:
    if numbers > max:
        max = numbers
    print(max)
