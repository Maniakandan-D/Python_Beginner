data = [4, 5, 104, 105, 110, 130, 120, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
# del data[0:2]
# print(data)

# del data[:4]
# print(data)
# print(data[10:])

min_valid = 100
max_valid = 200
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]
print(data)
