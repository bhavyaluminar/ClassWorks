# #IF-ELIF-ELSE
#
# #Maximum of 3 numbers
#
# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# n3=int(input("Enter the third number"))
# if(n1>n2 and n1>n3):
#     print("First number",n1,"is biggest")
# elif(n2>n1 and n2>n3):
#     print("Second number", n2, "is biggest")
# else:
#     print("Third number", n3, "is biggest")

#Maximum of 4 numbers
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
n4=int(input("Enter the fourth number"))
if(n1>n2 and n1>n3 and n1>n4):
    print("First number",n1,"is biggest")
elif(n2>n1 and n2>n3 and n2>n4):
    print("Second number", n2, "is biggest")
elif(n3>n1 and n3>n2 and n3>n4):
    print("Third number", n3, "is biggest")
else:
    print("fourth number", n4, "is biggest")

