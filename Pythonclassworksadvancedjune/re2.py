# #Match Function
#
# import re
# s="Hi Python Hello World"
#
# m=re.match(r'Hello',s)
#
# if(m):
#     print('match found')
# else:
#     print("no match")

#Search
# import re
# s="Hello Python Hello World"  #it returns only one match
#                               #it returns match object not list
# m=re.search(r'Hello',s)
#
# if(m):#if match object
#     print('match found')
#     print(m.group()) #To print the matching value
#     print(m.span())#To print the position of matching value
#     print(m.start())#to print the  starting position
#     print(m.end())#to print the end position
# else:
#     print("no match")


#SUB()
import re
s="john@abc.com and mike@pqr.com"
m=re.sub(r'@[a-z]+','@gmail',s) #@[a-z]+ starting with @ followed by lower case characters

print("updated string",m)

#SPLIT()
s="Python is a programming language"

m=re.split(r'\s',s)
print(m)
s="Python1 is a 2programming 3language"

m=re.split(r'\d',s)
print(m)

