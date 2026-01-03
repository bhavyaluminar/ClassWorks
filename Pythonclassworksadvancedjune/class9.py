#Single level

class Parent:
    def m1(self):
        print("in method m1")
    def m2(self):
        print("in method m2")

# p=Parent()
#
# p.m1()
# p.m2()
#syntax
#class classname(Parentclass)
class Child(Parent):
    def m1(self):
        #super().m1() #method overriding -used for modification/extending functionality inside Parent
                      #super() -to access parent attributes
        print("in child class")
    def m3(self):
        print('in method m3')
c=Child()
c.m1()
c.m2()
c.m3()