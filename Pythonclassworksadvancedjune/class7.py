#Menu driven code for Bank Operation using Class

# 1.Craete Account
# 2.Withdraw
# 3.DEposit
# 4.Showbalance
# 5.EXit

class Account:
    def __init__(self):
        print("Enter Account Details")
        self.acctnumber=int(input("Enter the account number"))
        self.acctname=input("Enter the account name")
        self.balance=int(input("Enter the balance"))
    def withdraw(self):
        amount=int(input("Enter the amount"))
        self.balance=self.balance-amount
    def deposit(self):
        amount = int(input("Enter the amount"))
        self.balance = self.balance +amount
    def showbalance(self):
        print("The Available Balance",self.balance)
l=[]
while(1):
    print("BANK OPERATIONS:-")
    print('1.Create Account')
    print('2.Deposit')
    print("3.Withdraw")
    print("4.ShowBalance")
    print("5.Exit")

    ch=int(input("Enter the choice"))
    if ch==1:
        a=Account()
        l.append(a)  #adding each account object into list
        print(l)
    elif ch==2:
        number = int(input("Enter the account number"))
        for i in l:
            if i.acctnumber == number:
                i.deposit()
                break
        else:
            print("Account does not exist")

    elif ch==3:
        number = int(input("Enter the account number"))
        for i in l:
            if i.acctnumber == number:
                i.withdraw()
                break
        else:
            print("Account does not exist")


    elif ch==4:
        number = int(input("Enter the account number"))
        for i in l:
            if i.acctnumber == number:
                i.showbalance()
                break
        else:
            print("Account does not exist")

    else:
        exit()

