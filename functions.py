def multiply(x, y):  # name of function is multiply() # we can also define an inside parenthesis
    result = x * y
    return result  # return to function so we used return statement


answer = multiply(11.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for value in range(1, 6):
    two_each = multiply(2, value)
    print(two_each)
