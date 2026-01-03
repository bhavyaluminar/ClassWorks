# #global
#
#
# x=10  #global -means it can be used anywhere inside the program
#
# print(x)  #10
#
# def f():
#      print(x)  #10
#
# f()
# print(x) #10

#local
# def f():
#     x = 10  # local
#     print(x)  # 10
#
#
# f()
# # print(x)
#
# def f():
#     global x #to make a local variable into global variable
#     x=10
#     print("Inside function f",x)
#
# def g():
#     print("inside function g",x)
#
# f()
# g()
#
# print(x)



#Enclosing
#
# def outer():
#     x = 10  # enclosing
#     print(x)
#
#     def inner():
#         y=30   #local
#         print(x)
#
#     inner()
#
#
# outer()





























