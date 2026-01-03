# # # # import re
# # # #Q1.Find all words starting with s,p or r and ends at 'at
# s="sat mat pat cat rat bat"
# import re
# a=re.findall(r'[spr]at',s)
# print(a)
#
#
#
# # #
# # # #Q2.Find all words starting with except s,p or r and ends at 'at'
# s="sat mat pat cat rat bat"
# a=re.findall(r'[^spr]at',s)
# print(a)
#
# # # #
# # # #Q3.Find all 3,4 and 5 digit numbers from the string
# s="123 6738 34556 355666 76767564 445222"
# a=re.findall(r'\b\d{3,5}\b',s)
# print(a)
# #
# # # # #
# # # # #Q4.Find all 3,4 and 5 letter words from the string
# # s="The quick brown fox jumps over the lazy dog"
# # s="123 6738 34556 355666 76767564 445222"
# # a=re.findall(r'\b[a-z]{3,5}\b',s)
# # print(a)
# # #
# # #Q5.Write a program to find filenames with particular extension
# import re
# s="s.html,k.txt,m.jpeg,l.py,a.jpeg"
#
# n=re.findall(r'[a-z]+.txt',s)
# print(n)
#
# #
# #Q6.Write a program to find words containing 'z' from a string
import re
s="abcdz abzcd zabcd hjklj"
m=re.findall(r'[a-z]*z[a-z]*',s)
print(m)


# #
#
#
# #Q7.Check whether the given string contains only lowercase, uppercase,digits and underscore
# import re
s="57767"

# # #Q8.Write a program to extract year/month/date from a url
import re
# s="www.washingtonpost.com/news/football-insider/wp/2016/09/02"
# n=re.findall(r'[0-9]{4}/[0-9]{2}/[0-9]{2}',s)
# print(n)
# #
# #Q9.Replace \n with space
#
s="""Keep the blue flag
flying high
Chelsea"""
n=re.sub(r'\n'," ",s)
print(n)


# #output:Keep the blue flag flying high Chelsea
#
# #Q10.Replace dot,comma and space  with :
# #
s="Python is a,Programming language."

n=re.sub(r'[. ,]',':',s)
print(n)

# # output:"Python:is:a:Programming:language:"
#
# #Q11.Remove all alphanumeric characters from the string
# # #
s="adfsgdhvj5678 &#%%^&& sfdhfhj _RfGGGG"
# #output:" &#%%^&&  _"

m=re.sub(r'[a-zA-Z0-9]','',s)

print(m)


# # # #Q12.Find all words starting with vowel and ends with vowel from the given string
# # # # # #
# s="red green orange"
# l=re.findall(r'\b[aeiou][a-z]+[aeiou]\b',s)
# print(l)
#
#
# # #Q13.Find the count of numbers in the string
# s="One 1 two 2 three 3 four 4456787"
#
# l=re.findall(r'\d',s)
# print(len(l))

#check whether a number is valid mobile number
n=input("Enter a number")
l=re.search(r'^[6789][0-9]{9}$',n)
if l:
    print('valid')
else:
    print('invalid')




