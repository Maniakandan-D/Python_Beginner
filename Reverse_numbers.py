class Reverse:

    def reverse_num(max, min):
        while max >= min:  # condition
            print(max, end=' ')  # same line not a new line
            max = max - 1  # max = max -1 til minimum number


max = int(input("Enter the max value: "))
min = int(input("Enter the min value: "))
print("List of number from {0} to {1} in reverse: ".format(max, min))  # 0, 1 index position
if __name__ == '__main__':
    Reverse.reverse_num(max, min)

# print()
# main code
# max = int(input("Enter the max value: "))
# min = int(input("Enter the min value: "))
# print("List of number from {0} to {1} in reverse: ".format(max, min))
# while max >= min:  # condition
#    print(max, end=' ')  # same line not a new line
#    max = max - 1  # max = max -1 til minimum number
