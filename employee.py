class Employee:
    def message(self):
        print("This is employee class")
class Company(Employee):
    def message(self):
        print("This is Company class")

emp = Employee()
emp.message()
comp = Company()
comp.message()
