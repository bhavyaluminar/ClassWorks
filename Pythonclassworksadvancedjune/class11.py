class Vehicle:
    def __init__(self):
        self.brand=input("Enter brand")
        self.model=input("Enter model")
        self.year=int(input("Enter year"))
    def display_info(self):
        print(self.brand,self.model,self.year)

class Car(Vehicle):
    def __init__(self):
        #super().__init__()
        Vehicle.__init__(self)
        self.cc=input("Enter cc")
    def display_info(self):
        #super().display_info()
        Vehicle.display_info(self)
        print(self.cc)
c=Car()
c.display_info()