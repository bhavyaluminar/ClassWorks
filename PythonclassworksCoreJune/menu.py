#MEnu driven Code for Arithmetic Operation

def add():
    n1=int(input("Enter number"))
    n2=int(input("Enter number"))
    s=n1+n2
    print(s)
def sub():
    n1=int(input("Enter number"))
    n2=int(input("Enter number"))
    s=n1-n2
    print(s)
def mul():
    n1=int(input("Enter number"))
    n2=int(input("Enter number"))
    s=n1*n2
    print(s)
def div():
    n1=int(input("Enter number"))
    n2=int(input("Enter number"))
    s=n1/n2
    print(s)
while(1):
    print("Arithmetic Operations")
    print('1.Addition')
    print('2.subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.exit')

    ch=int(input("Enter the choice"))
    if ch==1:
        add()

    elif ch==2:
        sub()

    elif ch==3:
        mul()

    elif ch==4:
        div()
    else:
        exit()

