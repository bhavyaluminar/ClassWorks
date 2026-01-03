# #print each colors
colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']
#
# #starting with 'b'
for i in colors:
    if(i[0]=="b"):
        continue
    print(i)
#
# #colors containing letter n
#
# for i in colors:
#     if 'n' in i:
#         print(i)
#print the fruitnames with length greater than 6
fruits = ['banana', 'orange', 'apple', 'avocado', 'pomegranate']
# for i in fruits:
#     if(len(i)>6):
#         print(i)

#print odd values
# d = {'a': 10, 'b': 35, 'c': 46, 'd': 90, 'e': 27}
# for i in d.values():
#     if i%2!=0:
#         print(i)

#
# #print countryname contains word 'land'
d = {'c1': 'India', 'c2': 'Myanmar', 'c3': 'Bangladesh', 'c4': 'Newzealand', 'c5': 'iceland'}
# for i in d.values():
#     if 'land' in i:
#         print(i)
#
# #print vowel characters in the given string
s = "python is a programming language"
# vowels="aeiouAEIOU"
# for i in s:
#     if i in vowels:
#         print(i)

#
# #print each words in the string
s = "python is a programming language"
# words=s.split()
# for i in words:
#     print(i)
#
# #print only string values
# l = ['a', 3, 'hello', 9.8, 'c', 20]
# for i in l:
#     if type(i)==str:
#         print(i)
# #
# # #print squares of each number
# l = [1, 2, 3, 4, 5, 6]
# for i in l:
#     print(i**2)
# #
# #print numbers contains digit 3
l = [123, 456, 234, 908, 567, 845, 125, 534]
for i in l:
    if '3' in str(i):
        print(i)

