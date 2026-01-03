
# #list comprehension
# l=[1,2,3,4]
# new=[i**2 for i in l]  #in each iteration adds i**2 to new list where i takes value from l
# print(new)
# new=[i**3 for i in l]  #in each iteration adds i**3 to new list where i takes value from l
# print(new)
# new=[5 for i in l]    #in each iteration adds 5 to new list where i takes value from l
# print(new)
#
# #create a new list with first letter from each word
#
# l=['dog','cat','deer','sheep','pig']
# new=[i[0] for i in l]
# # print(new)
#
#
# l=[12,67,23,80,16]
#
# #create a new list with even values
# new=[i for i in l if i%2==0]
# print(new)
# #create a new list with odd values
# new=[i for i in l if i%2!=0]
# print(new)
# #create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)
#
# #Given a list
fruits=['apple','banana','orange','pineapple','avocado']
#create a new list with elements whose length >5
new=[i for i in fruits if len(i)>5]
print(new)
##Given a list
l=[12,39,'hello',8.7,-98,-11,5,'python']
#create a new list with only string vvalues
new=[i for i in l if type(i)==str]
print(new)

# #create a new list with only positive values
# new=[i for i in l if type(i)!=str and i>0]
# print(new)
#
# #create a new list with float values
# new=[i for i in l if type(i)==float]
# print(new)
#
# #create a list with elements whose value is divisible by 3 in the range (1,100)
#
# new=[i for i in range(1,101) if i%3==0]
# print(new)
#
# #Given a string
# s="python programming"
# # vowels="aeiouAEIOU"
# new=[i for i in s if i in "aeiouAEIOU"]
# print(new)
# # create a new list with only vowels
# #
# # #given a dictionary
# d={101:'Arun',102:'Amal',103:'Anu'}
# new=[i for i in d.values()]
#
print(new)
# # create a new list with only names
# #
# # #given a dictionary
# d={'a':10,'b':15,'c':20,'d':25}
# # create a new list only even values
# new=[i for i in d.values() if i%2==0]
# print(new)
#
# #Given a string
# s="python is a programming language"
# #creating a list with length of each word
#
#
# new=[len(i) for i in s.split()]
# print(new)
#


#SET COMPREHENSION

# s="hello world"
# #Creating new set with only letters from s #set -Only unique values and unordered collection
# new={i for i in s if i!=" "}
# print(new)
#
# #creating new set with only vowels from s
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)

#Dictionary comprehension
# l=[10,20,30,40]

# # new={i:i**2 for i in l}  #keys are values from list and values are squares of each value
# # print(new)
#
# new={i:l[i] for i in range(len(l))} #keys are index and values are values from list
# print(new)



























