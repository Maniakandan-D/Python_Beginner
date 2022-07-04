class dog:
    # attributes
    # may be data or function
    a = 1
    b = 2

    def fun(self):
        print("the value is", self.a)
        print("the value is", self.b)


# driver code
Mani = dog()  # object instantiation
print(Mani.a)  # Accessing class attributes
Mani.fun()  # method through object


class Person:
    age = 22

    def hello(self):
        print("Hello, ")


# new object create
Mani = Person()
print(Person.age)
print(Person.hello)
Mani.hello()  # without any argument


class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_date(self):
        print(f'{self.real} + {self.imag}j')


num1 = Complex(2, 3)
num1.get_date()
