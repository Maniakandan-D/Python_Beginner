pangram = "The quick brown fox jumps over the lazy dog"

words = pangram.split()
print(words)

generated_list = [
    "9" "2" "4" " ",
    "3" "2" " ",
    "1" "3" "4" "2" " ",
]
value = "".join(generated_list)
print(value)

value_list = value.split()
print(value_list)

# replace the value in list
for index in range(len(value_list)):
    value_list[index] = int(value_list[index])
print(value_list)

# create a new list
integer_value = []
for value in value_list:
    integer_value.append(int(value))

print(integer_value)