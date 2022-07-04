# inheritance
class Staff:
    def __init__(self, role, subject, salary):
        self.role = role
        self.subject = subject
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role: ", self.role)
        print("Subject: ", self.subject)


class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Teacher", "Maths", 15000)


teacher = Teacher('Mani', 27)
print(teacher.__dict__)
