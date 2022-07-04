class Multiple:
    """Multiple Table"""

    def main(self: int):
        for i in range(1, 11):  # not include 11
            print(self, "x", i, "=", self * i)  # i = 1,2,3,4,...10


self = int(input("Enter the number: "))
print("The multiplication table of:", self)  # chosen number

if __name__ == '__main__':  # constructor
    Multiple.main(self)  # class name.function name(argument)
