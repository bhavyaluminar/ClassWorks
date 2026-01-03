# #LAMBDA
#
# #square of anumber
#
# s=lambda x:x**2
#
# print(s(2))
#
# #Cube of a number
#
# c=lambda x:x**3
#
# print(c(3))
#
# #addition of 2 numbers
# s=lambda a,b:a+b
# print(s(4,5))
#
# #addition of 3 numbers
# s=lambda a,b,c:a+b+c
# print(s(4,5,8))
#
# #square root of a number
# sqr=lambda x:x**0.5
# print(sqr(9))
# #name from the given list
# # l=['arun',25,'ekm']
# # n=lambda a:a[0]
# # print(n(l))
# #
# #
# #
# # #name from a dictionary
# # d={'name':'arun','age':25,'place':'ekm'}
# # #
# # n=lambda a:a['name']
# # print(n(d))
# #
# #
# # #
# # # #place from  a dictionary
# # # d={'name':'arun','age':25,'place':'ekm'}
# # # n=lambda a:a['place']
# # # print(n(d))
# # #
# # #
# # # #length of the string
# # # s="hello world"
# # # n=lambda a:len(a)
# # # print(n(s))
# #
# #
# # #MAP Function
# # #
# # # #create a list of squares
# # #
# # # l=[1,2,3,4]
# # #
# # # #map(function,sequence)
# # #
# # # print(map(lambda x:x**2,l))
# # #
# # # print(list(map(lambda x:x**2,l)))
# # # print(tuple(map(lambda x:x**2,l)))
# # #
# # # #Create a list of cubes
# # # l=[1,2,3,4]
# # #Create a list of names
# #
# # d=[{'name':'arun','age':25},{'name':'amal','age':23},{'name':'anu','age':24}]
# #
# # print(list(map(lambda x:x['name'],d)))
# # #
# # #
# # # #create a list of authors
# # d=[['book1','john',300],['book2','sam',200],['book3','mike',250]]
# # print(list(map(lambda x:x[1],d)))
# #
# # # #create a list of length
# # colors=['red','green','orange','yellow','blue']
# # print(list(map(lambda x:len(x),colors)))
# # #
# # # #create a list of square roots
# # l=[36,81,49,16]
# # print(list(map(lambda x:x**0.5,l)))
# #
# #
# # #FILTER
# #
# # n=[1,2,3,4,5,6,7,8,9,10]
# # #Filter even values
# # print(list(filter(lambda x:x%2==0,n)))
# # print(list(filter(lambda x:x%2!=0,n)))
# #
# #
# # #Given a list
# # l=[23,67,-12,90,-15,89,60]
# # #filter even values
# # print(list(filter(lambda x:x%2==0,l)))
# # #filter odd values
# # print(list(filter(lambda x:x%2!=0,l)))
# # #filter the even values greater than 50
# # print(list(filter(lambda x:x%2==0 and x>50,l)))
# # #filter those values that are divisible by 3 and 5
# # print(list(filter(lambda x:x%3==0 and x%5==0,l)))
#
# #REDUCE
#
# n=[1,2,3,4]
# #sum of sequence using reduce
# import functools
# print(functools.reduce(lambda x,y:x+y,n))
#
# #product of a sequence using reduce
# n=[1,2,3,4]
# import functools
# print(functools.reduce(lambda x,y:x*y,n))

#Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]


#Sum of positive even numbers
pe=list(filter(lambda x:x%2==0 and x>0,l)) #positive even
import functools
print(functools.reduce(lambda x,y:x+y,pe))

#Sum of Positive Odd numbers
po=list(filter(lambda x:x%2!=0 and x>0,l)) #positive odd
import functools
print(functools.reduce(lambda x,y:x+y,po))

#Sum of Negative Odd Numbers
no=list(filter(lambda x:x%2!=0 and x<0,l)) #negative odd
import functools
print(functools.reduce(lambda x,y:x+y,no))

#Sum of Negatve Even Numbers
no=list(filter(lambda x:x%2==0 and x<0,l)) #negative even
import functools
print(functools.reduce(lambda x,y:x+y,no))
#Count of Positive numbers
p=list(filter(lambda x:x>0,l)) #list of positive
print(len(p))
#Count of negative numbers
n=list(filter(lambda x:x<0,l)) #list of positive
print(len(n))


#Given a list
l=["Python","coding","is","easy","and","fun"]


# Create a new string "Python coding is easy and fun" from the given list l

import functools
print(functools.reduce(lambda x,y:x+" "+y,l))

















