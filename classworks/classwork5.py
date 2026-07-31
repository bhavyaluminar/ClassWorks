# #Check whether a number is an Armstrong number
#
# num=int(input("Enter a number"))
# s=str(num)
#
# l=len(s)
#
# sum=0
#
# for i in s:
#
#        sum=sum+int(i)**l
#
# if(sum==num):
#      print("Armstrong")
#
# else:
#      print("not")
# #Given a list
# l=[1,2,3,4]
# # create a new list with squares of each element
# # new=[]
# # for i in l:
# #     new.append(i**2)
# # print(new)
# #Given a list
# l=[12,67,59,23]
# #create a list with elements whose value is greater than 50.
# # new=[]
# # for i in l:
# #     if(i>50):
# #         new.append(i)
# # print(new)
# # create a new set with elements whose value is greater than 50
# # new=set()
# # for i in l:
# #     if(i>50):
# #         new.add(i)
# # print(new)
# # #Given a list
# # l=[1,2,3,4]
# #create a new dictionary where keys are numbers and values are squares of each number
# # new={}
# # for i in l:
# #     new[i]=i**2
# # print(new)
#
# ##create a list of 5 random numbers
# # new=[]
# # for i in range(5):
# #     n=int(input("enter the number"))
# #     new.append(n)
# #     #print(new)
# # print(new)
#
#
# #Find the factors of a number
# num=int(input("Enter a number"))
#
# for i in range(1,num+1):
#
#       if(num%i==0):
#
#               print(i)
#
#
# #find the fibinocci series
#
#
# a=0
# b=1
# for i in range(1,11):
#     print(a)
#     a,b=b,a+b


# for i in range(1,11):
#     if(i==5):
# #         break
# #     print(i)
# # else:#will execute when loop completes its iterations
# #     print("hello")
# #
# # i=1
# # while(i<=5):
# #     print(i)
# #     i=i+1
# # else:
# #     print("hello")
#
#
# num = int(input("Enter a number"))
#
# if (num > 1):  # if num is greater than 1
#
#     for i in range(2, num):  # [2....num-1]
#
#         if (num % i == 0):
#             print("not prime")
#             break
#     else:
#         print("prime")
#
#
# else:  # if num is either 0 or negative
#     print("number is neither prime nor composite")


num=int(input("Enter number"))
sum=0
for i in range(1,num):

      if(num%i==0):

         sum=sum+i

if(sum==num):
       print("Perfect number")

else:
    print("not perfect")



