
from abc import ABC,abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass



class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("Enter length"))
        self.breadth=int(input("Enter breadth"))

    def area(self):
        print(self.length*self.breadth)


    def perimeter(self):
        print(2*(self.length+self.breadth))
r=Rectangle()
r.area()
r.perimeter()
class Circle(Shape):
    def __init__(self):
        self.radius = int(input("Enter radius"))

    def area(self):
        print(3.14*self.radius **2)

    def perimeter(self):
        print(2 *3.14* self.radius)