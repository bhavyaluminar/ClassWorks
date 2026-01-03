#Write a program to check whether a number is Positive or negative

n=int(input("Enter a number"))
if(n>0):
    print("number",n,"is positive")
else:
    print("number",n,"is negative")


#Write a program to check whether a number is even or odd
n = int(input("Enter a number"))
if (n %2 == 0):
    print("number", n, "is even number")
else:
    print("number", n, "is odd number")

#Write a program to check a number is multiple of 3 or not

n = int(input("Enter a number"))
if (n %3==0):
    print("number", n, "is multiple of 3")
else:
    print("number", n, "is not a multiple of 3")
