class Staff:
    def college(self, age):
        self.age = age
        print("age is: ", self.age)

    def school(self):
        print("age is: ", self.age)


mani = Staff()
mani.college(1)
mani.school()

mani1 = Staff()
mani1.college(10)
mani1.school()

del mani.age
mani1.school()

Staff.m = 11
mani_3 = Staff()
print("Staff.m: ", Staff.m)
print("mani.m: ", mani.m)
print("mani1.m: ", mani1.m)
print("mani_3.m: ", mani_3.m)

mani1.a = 22
print("mani1.a: ", mani1.a)

