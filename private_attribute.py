# Private attribute
# encapsulation
class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # Private attribute prefix__

    def details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.__salary)


staff = Teacher('mani', 22, 25000)
staff.details()
# staff._Teacher__salary  # we cannot access the attribute
print()
print("Outside the class ")
print(staff.name)
print(staff.age)
# print(staff.__salary)  # AttributeError: 'Teacher' object has no attribute '__salary'
# # outside the class not working
# print(staff._Teacher__salary)
