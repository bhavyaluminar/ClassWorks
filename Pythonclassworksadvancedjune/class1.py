class Person:
    def __init__(self,n,a): #__init__ constructor method to create and initialize
                            #object attributes
        self.name=n         #here name and age are attributes of object
        self.age=a          #self represents current object

    def showdetails(self):    #method
        print(self.name,self.age)

p1=Person('Arun',23)  #creates object p1 of class Person
                           #it will call __init__() inside the class
print(type(p1))            # shows class 'Person'
p2=Person('Amal',25) #creates object p2 of class Person
                            #it will call __init__() inside the class
# print(type(p2))           # shows class 'Person'
#objectname.attribute
#objectname.method()

p1.showdetails()
p2.showdetails()

print(p1.name,p2.name)
print(p1.age,p2.age)
