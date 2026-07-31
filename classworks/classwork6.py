# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5

# # 2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]

# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25


# 4.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90

# for i in range(0,len(l)):
#     print(l[i])


#5.Given a list, sum the elements until a 0 is encountered (stop at 0).
l=[4,9,1,0,6,7]


# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.


# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.



# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]


# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"


#
# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
l=[5,2,8,6,2]

# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"

s="abc123x7z"
digits="0123456789"
new=""
for i in s:
    if(i in digits):
        new=new+i
print(new)



# 12.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]

# 13.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"



# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
#
#
# 15.
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# #print all names of students

# for i in d.values:
#     print(i[0])

#
# 16.Write a program to print the numbers from 1 to 100.
# But for multiples of:
#
# 3, print “Fizz” instead of the number
#
# 5, print “Buzz” instead of the number
#
# Both 3 and 5, print “FizzBuzz”
#
# Otherwise, print the number itself
#
# Output format example:
# 1, 2, Fizz, 4, Buzz, … , FizzBuzz, …
#
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
#     Stop the loop if the number becomes greater than 40 using break
#
# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
#     sum of digits in  a number
#

