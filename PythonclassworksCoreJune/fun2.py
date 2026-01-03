#Using Parameters

#Sum of two numbers
# def add(n1, n2):
#     s = n1 + n2
#     print(s)
# #
# #
# # add(20, 50)
#
# #define function to calculate simple interest
# #si=p*n*r/100
# # p-amount(1000)
# # n-years(2)
# # r-rate (6)
#
# def simple_interest(p,n,r):
#     si=p*n*r/100
#     # print(si)
#     return si
#
#    #return statement is used to exit from a function
#    #optionally used to send function result to caller
#
# s=simple_interest(1000,2,6)
# print(s)

#Multiple return values

# def arithmetic_op(n1,n2):
#     s=n1+n2
#     d=n1-n2
#     p=n1*n2
#     q=n1/n2
#     return s,d,p,q #we can return  muliple results in a return statement
#
# s,p,d,q=arithmetic_op(40,2)
# print(s,d,p,q)

#Arbitary Argument type
#Non keyword
# def fun(*args): #Tuple
#     print(args)
#     for i in args:
#         print(i)
#
# fun(1,2,3)
# fun(5,6,7,8,9)
# fun(10,20,30,40)

#keyword
# def fun(**kwargs):     #Dictionary
#     print(kwargs)
#     for i,j in kwargs.items():
#         print(i,j)

# fun(name="arun")
# fun(name="amal",age=23)
# fun(name="anu",age=25,place="ekm",course="python")
































