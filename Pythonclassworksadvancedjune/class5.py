class Student:
    def __init__(self):
        self.rollno=int(input("Enter the roll number"))
        self.name=input("Enter the name")
        self.age=int(input("enter the age"))
        self.place=input("Enter the place")
    def showdetails(self):
        print(self.rollno,self.name,self.age,self.place)

s1=Student()
s2=Student()

s1.showdetails()
s2.showdetails()