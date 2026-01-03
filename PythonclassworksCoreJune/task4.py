# # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         continue
#     if(i%3==0 or i%3==0):
#         print(i)
#
#
# # 2.Take a string input from the user and print the reverse using a for loop.(without [::-1])
# n=input("Enter a string")
# rev=""
# for i in n:
#     rev=i+rev
# print(rev)
#
# #
# #3.Given a number n, write a program that uses a for loop to compute the sum of its digits.
# # Example: n = 1234 → Output: 10
# n=int(input("Enter a number"))
# s=str(n)
# sum=0
# for i in s:
# #     sum=sum+int(i)
# # print(sum)
# # #
# # 4.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
# # l=[1,2,3,4]
# # sum=0
# # for i in l:
# #     sum=sum+i
# #     print(sum)
#
#
# #
# # 5.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
# a,b=3,7
# sum=0
# for i in range(a,b+1):
#     sum=sum+i
# print(sum)
#
# 6.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90
# l=[10, 20, 30, 40, 50]
# sum=0
# for i in range(0,len(l),2):
#     print(l[i])
#     sum=sum+l[i]
# print(sum)
#7.Given a list, sum the elements until a 0 is encountered (stop at 0).
# Example: [1, 3, 5, 0, 8, 10] → Output: 9
l=[1, 3, 5, 0, 8, 10]
sum=0
for i in l:
    if i==0:
        break
    sum=sum+i
print(sum)


# 8.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
for i in range(1,1001):
    if(i%7==0 and i%11==0):
        print(i)
        break

# 9.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
l=['orange','apple','banana','kiwi']
for i in l:
    if(len(i)<5):
        continue
    print(i)
# 10. Loop from 1 to 30 and print all numbers except those divisible by 4. Use continue.
#
# 11.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]
# 12Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
s="hello world"
new=""
vowels="aeiou"
for i in s:
    if i in vowels:
        continue
    new=new+i
print(new)
#
# 13.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# .
#
# 14.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
s="abc123x7z"
digits="0123456789"
new=""
for i in s:
    if i in  digits:
        new=new+i
print(new)


# 15.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]
# 16.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"
# 17.From a list of numbers, create a list where each element is the cumulative product so far.
# Input: [2, 3, 4] → Output: [2, 6, 24]
# l=[2,3,4]
# product=1
# new=[]
# for i in l:
#     product=product*i
#     new.append(product)
# print(new)
# 18.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
#
