data = [105, 12, 123, 106, 202, 347, 126, 90, 3,
        234, 100, 103, 108, 300]

min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, - 1, - 1):
#    if data[index] < min_valid or data[index] > max_valid:
#       print(index, data)
#        del data[index]
# data = sorted(data)
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)
