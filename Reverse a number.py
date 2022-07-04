# Find Reverse Number
num = int(input("Please Enter the Reverse Numbers: "))
# print(str(num)[::-1]) if you want one line use this code
# You want line by line number use given code
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num*10 + digit
    num = num // 10
    print(" Reversed number is : "+str(reversed_num))

