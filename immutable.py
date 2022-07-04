result = True
another_result = result
print(id(result))  # return the identity of an object
print(id(another_result))

result = False
print(id(result))

# immutable object can't be changed
