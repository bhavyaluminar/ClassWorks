# #Factorial
# #
# # num=int(input("Enter a number"))
# # fact=1
# #
# # i=1
# # while(i<=num):
# # #     fact=fact*i
# # #     i=i+1
# # #
# # # print(fact)
# #
# # #
# # # num=int(input("Enter a number"))
# # # fact=1
# # # for i in range(1,num+1):
# # #     fact=fact*i
# # # print(fact)
# #
# # #Factors
# # num=int(input("Enter number"))
# #
# # for i in range(1,num+1):
# #
# #         if(num%i==0):
# #
# #               print(i)
# # #Armstrong
# n=int(input("Enter a number"))
# sum=0
# s=str(n)
# l=len(s)
#
# for i in s:
#     sum= sum+int(i)**l
# print(sum)
# if(sum==n): #compares sum and number
#      print("Armstrong")
#
# else:
#     print("Not Armstrong")

#Prime Number


num = int(input("Enter a number"))
if num>1:
    for i in range(2, num):

        if (num % i == 0):
            print("Not prime")

            break

    else:
        print("prime")
else:
    print('not prime')









