class Employee():
    def __init__(self):
        self.name = name
        self.deignation = des
    def disp1(self):
        return f"Employee's name is : {self.name}"
        return f"Employee's designation is: {self.deignation}"
class Salary(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.salary = sal
    def disp2(self):
        return f"Salary of employee is: {self.salary}"
name = input("Enter Name : ")
des = input("Enter Designation: ")
sal = int(input("Enter Salary: "))        
s = Salary()
emp = Employee()
print(emp.disp1())
print(s.disp2())


