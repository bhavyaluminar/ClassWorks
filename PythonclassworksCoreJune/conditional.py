# # write a program to check whether an entered character is vowel or not
# ch=input("Enter a character")
# vowels="aeiouAEIOU"
# if(ch in vowels): #if entered character is present in vowels sequence
#     print("Vowel")
# else:          #if not present in vowels sequence
#     print("not a vowel")
# #write a program to check whether the last digit of a number is divisible by 3 or not


#1st method
# n=int(input("Enter the number"))
# last_digit=n%10    #last_digit of a number
# if(last_digit%3==0): #to check last digit is divisible by 3
#     print("last digit is divisible by 3")
# else:
#     print("not divisible by 3")

#2nd method
# n=int(input("Enter the number"))
# s=str(n)
# if(int(s[-1])%3==0): #last character of a string
#     print("last digit is divisible by 3")
# else:
#     print("not divisible")



# # #write a program to check whether the entered number is  a 2 digit number
# num=int(input("Enter number"))
# if(10<=num<=99): #if number is between 10 and 99
#     print("number is 2 digit")
# else:
#     print("not a 2 digit number")

# write a program to check whether the two strings are equal or not
# s1=input("Enter the first string")
# s2=input("Enter the second string")
# if s1==s2:
#     print("strings are equal")
# else:
#     print('not equal')

#
# #write a program to check whether a string is palindrome or not
# s=input("Enter a string")
# rev=s[::-1]
# print(rev)
# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#write a program to check an entered number is present in the given list or not
# l=[1,2,3,4,5,6]
# n=int(input("Enter a number"))
# if n in l:
#     print("Present")
# else:
#     print('not present')

#
# #write a program to check a particular key is present in a dictionary or not
# d={100:'Arun',101:'Amal',102:'Anu'}
# key=int(input("Enter key value "))
# if key in d:
#     print("key is present")
# else:
#     print("not present")

#Write a program to check whether the entered "location name" contains the word 'land'
# location_name=input("Enter the location name")
# if 'land' in location_name:
#     print('present')
# else:
#     print('not present')

#write a program to find the maximum of two numbers
# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# if(n1>n2):
#     print("first number is biggest")
# else:
#     print("second number is biggest")


