print("Please select the operation:"
      """
1: Add
2: Subtract
3: Multiply
4: Divide
 """)
i = int(input("Select the operation from 1, 2, 3, 4: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if i == 1:
    c = a + b
    print(f'{a} + {b} = {c}')  # f' string
    # print('{} + {} = {}'.format(a, b, c)) # formatted string
elif i == 2:
    c = a - b
    print('{} - {} = {}'.format(a, b, c))
elif i == 3:
    c = a * b
    print('{} * {} = {}'.format(a, b, c))
elif i == 4:
    c = a // b
    print('{} // {} = {}'.format(a, b, c))
else:
    print("Please enter 1 to 4")
