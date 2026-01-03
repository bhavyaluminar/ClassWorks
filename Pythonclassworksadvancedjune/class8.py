class Book:
    # book_no
    # title
    # author
    # price
    # pages
    # language
    def __init__(self):
        print("Enter Book Details")
        self.book_no=int(input("Enter Book number"))
        self.title=input("Enter title")
        self.author=input("Enter the author")
        self.price=int(input("Enter the Price"))
        self.pages=int(input("Enter the Pages"))
        self.language=input("Enter language")

    def showdetails(self):
        print(self.book_no,self.title,self.author,self.price,self.pages,self.language)
    def updatebook(self):

        choice = input("Enter the Choice:title/author/all")
        if choice == "title":
            self.title = input("Enter new title")
        elif choice == "author":
            self.author = input("Enter new author")
        elif choice == "all":
            self.title = input("Enter new title")
            self.author = input("Enter the new author")
            self.price = int(input("Enter the new Price"))
            self.pages = int(input("Enter the new Pages"))
            self.language = input("Enter the new language")
        else:
            pass

    def deletebook(self):
        l.remove(self)
        print("Book with book number",self.book_no,"is deleted")


l=[]
while True:
    print("Library Operations")
    print('1.Add Book Details')
    print('2.Show All Books')
    print('3.Read A Specific Book')
    print('4.Update A Book')
    print('5.Delete A Book')
    print('6.Exit')

    ch=int(input("Enter the choice"))
    if ch==1:
        b=Book()
        l.append(b)
    elif ch==2:
        for i in l:
            i.showdetails()
    elif ch==3:
        booknumber=int(input("Enter number"))
        for i in l:
            if i.book_no==booknumber:
                i.showdetails()
                break
        else:
            print("Book does not exist")

    elif ch==4:
        booknumber = int(input("Enter number"))
        for i in l:
            if i.book_no == booknumber:
                i.updatebook()
                break
        else:
            print("Book does not exist")

    elif ch==5:
        booknumber = int(input("Enter number"))
        for i in l:
            if i.book_no == booknumber:
                i.deletebook()
                break
        else:
            print("Book does not exist")
    else:
        exit()


