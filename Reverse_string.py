a = (input("Please enter your own: "))
b = ''
i = len(a) - 1
while i >= 0:
    b = b + a[i]
    i = i - 1

print("\nthe reverse original string is :", a)
print("The reverse string: ", b)
