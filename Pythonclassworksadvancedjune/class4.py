class Book:
    def __init__(self):
        self.bookno=int(input("Enter the bookno"))
        self.title=input("Enter book title")
        self.author=input("Enter author")
        self.price=int(input("Enter price"))
        self.language=input("Enter language")
    def gettitle(self):
        print("Title",self.title)
        return
    def getauthor(self):
        print("Author", self.author)
    def getprice(self):
        print("Price", self.price)

    def settitle(self):
        self.title=input("Enter the new title")
        self.gettitle()

    def setauthor(self):
        self.author = input("Enter the new author")
        self.getauthor()

    def setprice(self):
        self.price = input("Enter the new price")
        self.getprice()

b=Book()
b.gettitle()
b.settitle()