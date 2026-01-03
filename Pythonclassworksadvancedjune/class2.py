#dynamic
class Person:
    def __init__(self):
        print("Enter the details")
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))

    def showdetails(self):
        print(self.name,self.age)

p1=Person()
p2=Person()

p1.showdetails()
p2.showdetails()

print(p1.name,p2.name)
print(p1.age,p2.age)
