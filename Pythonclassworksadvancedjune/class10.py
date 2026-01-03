#Company-Employee
class Company:
    def __init__(self):
       self.company_name=input("Enter Company name")
    def show_company(self):
        print("Company Name",self.company_name)
class Employee(Company):
    def __init__(self):
        super().__init__()
        self.name=input("Enter name")
        self.age=int(input("Enter age"))
        self.empid=int(input("Enter emp id"))
        self.salary=int(input("Enter salary"))

    def get_salary(self):
        print("Employee Id",self.empid,"Salary",self.salary)
e=Employee()
e.get_salary()
e.show_company()

