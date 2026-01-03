class Employee:
    def __init__(self):
        self.empid=int(input("Enter the employee id"))
        self.name=input("Enter name")
        self.age=int(input("Enter age"))
        self.salary=int(input("Enter salary"))
        self.designation=input("Enter designation")

    def show(self):
        print(self.empid,self.name,self.age,self.salary,self.designation)

    def getsalary(self):
        print(self.salary)



e1=Employee()
e1.show()
e1.getsalary()