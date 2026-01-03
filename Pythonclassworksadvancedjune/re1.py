# s="""John is 45 and Sam is 13
#     Mike is 36 and Jose is 80"""
#
# import re
#
# names=re.findall(r'[A-Z][a-z]+',s)
# #[A-Z][a-z]+  -->starting with capital letter followed by lowercase letters
# print(names)
#
# ages=re.findall(r'\d{2}',s)
# print(ages)
# #[0-9]{2} -exactly 2 combination of digits

#
# #Given
# s="Sam John Jose Mike"
# import re
# #find the names starting with 'J'
# # names=re.findall(r'J[a-z]+',s)
# # print(names)
# # #
# # import re
# # s="abd abcd abccd abcccd abed"
# #
# #
# # l=re.findall(r'abc*d',s)
# # print(l)
#
# import re
# #Find all words starting with s,p or r and ends at 'at'
# s='sat mat pat rat cat bat'
# #pattern='[spr]at'
# l=re.findall(r'[spr]at',s)
# print(l)
#
# #Find all words starting with except s,p or r and ends at 'at'
#
# s="sat mat pat rat cat bat"
#
# #pattern='[^spr]at'
# l=re.findall(r'[^spr]at',s)
# print(l)
# #Given
# s="567 123456  1234  8903 4567892"
#
# #find all 3 digit,4 digit and 5 digit numbers from the string
# #pattern='\d{3,5}'
# l=re.findall(r'\d{3,5}',s)
# print(l)
#
# #Given
# s="the quick brown fox jumps over the lazy dog"
#
# # find all 3 letter,4 letter and 5 letter words from the string.
# # pattern='[a-z]{3,5}'
# l=re.findall(r'\b[a-z]{3,5}\b',s)
# # print(l)
#
#
# #\b --non word character boundary except digit letter or underscore
# import re
# s="hello_world  2hello2world  hello world  :hello:world helloworld"
#
# l=re.findall(r'\bhello\b',s)
# print(l)














