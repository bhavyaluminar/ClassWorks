#Method Overloading

class A:
    def show(self):
        print("hello")
    def show(self,a):
        print(a)
    def show(self,a,b):       #valid
        print(a,b)

obj=A()
# obj.show()  #it shows error while calling
# obj.show(10) #it shows error while calling
obj.show(20,30) #it will call last defined show method.