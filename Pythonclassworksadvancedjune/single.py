#Single level

class Person:
    def __init__(self):
        self.name=input("Enter name")
        self.age=int(input("Enter age"))
    def show(self):
        print(self.name,'\n',self.age,'\n')
# p=Person()

class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input("Enter rollnumber"))
        self.course=input("Enter course")
    def show(self):
        super().show()
        print(self.rollno,self.course)

s=Student()
s.show()