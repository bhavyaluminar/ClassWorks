#
# # i=7
# # while(i<=70):
# #     print(i)
# #     i=i+7
# #
# # 7,14,21,28,35,42,49,56,63,70
#
#
# #print those numbers whose value is greater than 50
# l=[24,50,12,33,45,53,90]
# for i in l:
#     if(i>50):
#         print(i)
#
# #create a new list with elements whose value greater than 50.
# l=[24,50,12,33,45,53,90]
# new=[] #Empty list
# for i in l:
#     if(i>50):
#         new.append(i)
# print(new)
#
# #create a new set with elements whose value grater than 50
# l=[24,50,12,33,45,53,90]
# new=set() #Empty set
# for i in l:
#     if(i>50):
#         new.add(i)
# print(new)

#write a program to print each digit in a number
# # n-1234
# n=int(input("Enter a number"))
# s=str(n)
# # for i in s:#1234
#    print(i)
# #list
# new=[]
# for i in s:
#     new.append(i)
# print(new)

#string
# new=""
# for i in s:
#     new=new+i
#     print(new) #1234
# print(new)
#set
# new=set()
# for i in s:
#     new.add(i)
# print(new)

#Given a string
# s="hello world"
#
# # new=""
# #
# # for i in s:
# #     new=new+i
# # print(new)
#
# #"dlrow olleh"
# #Reverse a string  without using s[::-1]
#
# # new=""
# #
# # for i in s:
# #     new=i+new
# #     print(new)
# # print(new)
#
# #1.Write a program to reverse a number
# n=int(input("Enter a number"))
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print("Reversed String",rev)
# #2.create a new list with even values from the given dictionary
#
# d={'n1':10,'n2':15,'n3':56,'n4':91,'n5':80}
# new=[]
# for i in d.values():
#     if(i%2==0):
#         new.append(i)
# print(new)

#3.write a program to find the sum of digits in a number

# # for eg:
# #     n-1234
# #     reult-1+2+3+4 =10
# n=int(input("Enter a number"))
# s=str(n)
# sum=0
# for i in s:
#     sum=sum+int(i)
# print(sum)


#Given a list
l=[11,45,67,23,89,66,30]
#print the elements
for i in l:
    print(i)
#print the even values
for i in l:
    if(i%2==0):
        print(i)
#sum of elements
sum=0
for i in l:
    sum=sum+i
print(sum)
#print the numbers greater than 50
for i in l:
    if(i>50):
        print(i)






















