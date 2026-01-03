
#
# def decorator_fun(fun):
#     def wrapper_fun(a,b):
#         if(a<b):  #extra functionality to swap the arguments if the first number is smaller than second
#             a,b=b,a
#         return fun(a,b) #calls the normal fun.In this case sub(a,b)
#     return wrapper_fun
#
#
# @decorator_fun
# def sub(a,b):
#     # if(a<b):
#     #     a,b=b,a
#
#     return a-b
#
#
# print(sub(10,5))
#
# print(sub(5,10))

def decorator_fun(fun):
    def wrapper(a,b):
        if(b==0):
            return "can't divide by zero"
        else:
            return fun(a,b)
    return wrapper

@decorator_fun
def div(a,b):
    return a/b


print(div(10,2))
print(div(10,0))

#define a decorator to check the second operand is zero before calling div(a,b).




