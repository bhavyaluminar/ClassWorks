class Circle:
    def __init__(self):
        self.radius=int(input("Enter radius"))
    def getarea(self):
        area=3.14*self.radius**2
        print("Area",area)

    def getperimeter(self):
        peri=2*3.14*self.radius
        print("Perimeter",peri)
c1=Circle()
c2=Circle()
# c1.getarea()
# c1.getperimeter()
#
# c2.getarea()
# c2.getperimeter()
# print(l[0].radius)
# l[0].getarea()
# l[0].getperimeter()
# print(l[1].radius)

l=[c1,c2]
for i in l:
    print(i.radius)
    i.getarea()
    i.getperimeter()






