class Function:
    def __init__(self, num):
        self.num = num

    # adding Two Objects
    def __add__(self, num1):
        return self.num + num1.num

    # comparison operator
    def __gt__(self, num1):
        if self.num > num1.num:
            return False
        else:
            return True


operator = Function(10)
operator_1 = Function(2)
operator_2 = Function('Manikandan')
operator_3 = Function(' D')
print(operator + operator_1)
print(operator_2 + operator_3)
print()
if operator > operator_1:
    print("operator is greater than operator_1")
else:
    print("operator is less than operator_1")
