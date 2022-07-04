class numbers:

    def main(self: float):
        if self > 1:
            print("This is  Positive Number")
        elif self == 0:
            print("it's zero")
        else:
            print("This is  negative number")


self = float(input("Enter the number: "))
if __name__ == '__main__':
    numbers.main(self)
