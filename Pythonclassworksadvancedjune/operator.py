class A:
    def __init__(self):
        self.x=int(input("Enter number"))
        self.y=int(input("Enter number"))
    def __add__(self,other):
        return self.x+other.x



obj1=A()
obj2=A()

print(1+2)  #int+int

print(obj1+obj2)