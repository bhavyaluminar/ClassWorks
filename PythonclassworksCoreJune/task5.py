#print series 1,4,7,10,13,16 using while loop
#
# i=1
# while(i<=16):
#     print(i,end=" ")
#     i=i+3
# print()
#for loop
# for i in range(1,17,3):
#     print(i,end=" ")

#print the sum and product of the series 8,6,4,2 using for loop
# sum=0
# prod=1
# for i in range(8,1,-2):
#     sum+=i
#     prod*=i
# print(sum,end=" ")
#
# print(prod,end=" ")
# given a list l=['dog','cat','deer','sheep','pig'] print the first letter from each words
# l=['dog','cat','deer','sheep','pig']

#in string format
# # m=""
# # for i in l:
# #     m=m+i[0]
# # print(m)

#list
# p=[]
# for i in l:
#     p.append(i[0])
# print(p)

#Given a list
# l=['dog','cat','deer','sheep','pig']
#print animal names starting with d
# for i in l:
#     if i[0]=="d":
#         print(i,end=" ")
# print()
# # #print the animal names contains "e"
# for i in l:
#     if 'e' in i:
#         print(i,end=" ")
#
# #print the first animal name starting with letter 'd'
#
# for i in l:
#     if i[0]=="d":
#         print(i)
#         break
#print the animal names starting with except "d"
# for i in l:
#     if(i[0]=="d"):
#         continue
#     print(i)


#count of 4 digit numbers that are divisible 4 and 3

# count=0
# for i in range(1000,10000):
#     if(i%4==0 and i%3==0):
#         count=count+1
# print(count)

#Given a string
s="python is a programming language"
#creating a dictionary where keys are words and values are the length of each word.

# words=s.split()
# for i in words:
#     print(i)
#output -->d ={'python':6,'is':2,'a':1,'programming':11,'language':8}
# words=s.split()
# d={}
# for i in words:
#     #print(i)
#     d[i]=len(i)  #words are keys and lengths are values
#
# print(d)

#print each digit in a number

# n=int(input("Enter a number"))
# s=str(n)
# for i in s:
#     print(i)

#reverse of a number

# n=int(input("Enter a number"))
# s=str(n)
# m=""
# for i in s:
#     m=i+m
# print(m)
#sum of digits
# n=int(input("enter a number:"))
# s=str(n)
# # sum=0
# # for i in s:
# #     sum=sum+int(i)
# # print(sum)
# #check whether a number is armstrong number or not
# n=int(input("enter a number:"))
# s=str(n)
# length=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**length
# if sum==n:
#     print("it is  armstrong")
# else:
#     print("not armstrong")

#Print the Pattern

# 1
# # 1 2 3
# # 1 2 3 4 5
#
# for i in range(1,6,2):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#print the character at the even index position
# s="hello world"
# for i in range(0,12,2):
#     print(s[i])
#fibinocci series
# n=int(input("Enter the term:"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     # c=a
#     # a=b
#     # b=a+c
#     a,b=b,a+b

# # factors of a number
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

#Prime number

# n=int(input("Enter a number"))
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             print('not prime')
#             break
#
#     else:
#         print('prime')
# else:
#     print('not prime')









