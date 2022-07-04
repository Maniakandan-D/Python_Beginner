class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        return self.a + b.a

    def __gt__(self, b):
        if self.a > b.a:
            return False
        else:
            return True


obj = A(12)
obj2 = A(2)
print(obj + obj2)
print()
print(obj > obj2)
