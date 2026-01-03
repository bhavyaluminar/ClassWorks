# # # #write a program to check whether the entered number is 2 digit/3digit/4 digit number
# # n=int(input("Enter the number"))
# # if(10<=n<=99):
# #     print("2 digit")
# # elif(100<=n<=999):
# #     print("3 digit")
# # # elif(1000<=n<=9999):
# # #     print("4 digit")
# # # else:
# # #     print("number is either single digit or more than 4 digit")
# #
# # # # #write a program to print the Grade of a student based on entered score
# # # #
# # # # 91-100    Grade A
# # # # 81-90     Grade B
# # # # 71-80     Grade C
# # # # 61-70     Grade D
# # # # below 61  Grade E
# #
# # score=int(input("Enter the score"))
# # if(91<=score<=100):
# #     print('Grade A')
# # elif(81<=score<=90):
# #     print('Grade B')
# # elif(71<=score<=80):
# #     print('Grade C')
# # elif(61<=score<=70):
# #     print('Grade D')
# # elif(score<61):
# #     print("Grade E")
# # else:
# #     print("Invalid Score")
#
# # # #Write a Basic Calculator program to perform Arithmetic Operations(+,-,*,/)
# #
# # n1=int(input("Enter the number"))
# # n2 =int(input("Enter the number"))
# # op=input("Enter the operator +/-*")
# # if(op=='+'):
# #     print("Sum",n1+n2)
# # elif(op=='-'):
# #     print("Difference",n1-n2)
# # elif(op=='*'):
# #     print('Product',n1*n2)
# # elif(op=='/'):
# #     print("Quotient",n1/n2)
# # else:
# #     print("Invalid Operation")
#
# # #Write program to print the number of days in  a month
#
# month_name=input("Enter the monthname")
# l1=['january','march','may','july','august','october','december']
# l2=['april','june','september','november']
# l3=['february']
#
# if month_name in l1:
#     print("number days in",month_name,"is 31 days")
# elif month_name in l2:
#     print("number days in", month_name, "is 30 days")
# elif month_name in l3:
#     print("number days in",month_name,"is 28 days")
# else:
#     print("invalid")


#Using Dictionary
# d={'january':31,'february':28,'march':31}
# month_name=input("Enter month")
# if month_name in d:
#     print("Number of days",d[month_name])
# else:
#     print("invalid")













