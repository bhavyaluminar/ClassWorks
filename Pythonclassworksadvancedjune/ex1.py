# try:
#     n1=int(input("Enter number"))
#     n2=int(input("Enter number"))
#     r=n1/n2
#
# except:
#     print("Zero division Error")
# else:
#     print("result",r)
#
# #write a program that takes a number as input from user and finds the factorial of that number
# #using math.factorial.Use a try -except block to handle the value error if user inputs
# #negative number/a character input
#
import math
#1
while(1):
    try:
        n=int(input("Enter a number"))
        m=math.factorial(n)

    except:
        print("value error")
    else:
        print(m)
        break

#2
def f():
    try:
        n=int(input("Enter a number"))
        m=math.factorial(n)

    except:
        print("value error")
        f()          #recursive function
    else:
        print(m)


f()







# #write a program to open a file(eg a text file)in read mode.if the file does not exist catch
# #the exception print error message file does not exist.
# try:
#     file_name=input("Enter the filename")
#     f=open(file_name,'r')
#     print(f.read())
# except:
#     print("File Does not Exist")
# else:
#     pass

# try:
#     n1=int(input("Enter number"))
#     n2=int(input("Enter number"))
#     r=n1/n2
# except ZeroDivisionError as e:
#     #print("Zero division Error")
#     print(type(e),e) #type of exception and description
# except ValueError as s:
#     #print("ValueError")
#     print(type(s),s)
# except Exception as e:
#     #print("error occured")
#     print(e)
# else:
#     print("result",r)
#
# finally:
#     print('hello')
#
#
#
