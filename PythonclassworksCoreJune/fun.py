#
# #function definition
# def add():
#     "ADDITION OF TWO NUMBERS"  #Function Docstring
#     n1=int(input("Enter number"))
#
#     n2=int(input("Enter number"))
#
#     s=n1+n2
#     print("sum",s)
#     return    #Used to exit from the function
#
# add()   #Function call

#define a function to find the factorial of a number

# def fact():
#     n=int(input("Enter a number"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print("factorial is",f)
#
# fact()

#
# #Define a function to find the reverse of a string
# # def reverse():
# #     s=input("Enter a string")
# #     r=""
# #     for i in s:
# #         r=i+r
# #     print("Reversed string",r)
# # reverse()
# #Define a function to check whether a number is prime or not
#
# def prime():
#     n=int(input("Enter a number"))
#     if n>1:
#         for i in range(2,n):
#             if(n%i==0):
#                 print('not prime')
#                 break
#         else:
#             print("prime")
#     else:
#         print("not prime")
# prime()

#Define a function to find BMI  (bmi -weight in kg/(height in m **2) )

def bmi():
    w=int(input("Enter weight in kg"))
    h=int(input("Enter height in m"))
    b=w/(h**2)
    print("BMI",b)
bmi()