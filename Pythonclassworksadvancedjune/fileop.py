#
#
# #Write a program to print the number of lines in a file
# f=open('k.txt','r')
# content=f.readlines() #list of lines
# print(len(content))
#
#
# #write a program to print the number of words in a file
# f=open('k.txt','r')
# content=f.read()
# # words=content.split() #list of words
# # print(len(words))
#
#
# #write a program to read the last 5 lines from a file
# # f=open('k.txt','r')
# # content=f.readlines()
# # for i in range(-5,0):
# #     print(content[i])
#
# #write a program to change the second line in a file
# # f=open('k.txt','r')
#
# # content=f.readlines()
# # content[1]="line2 is changed\n"
# #
# # f=open('k.txt','w')
# # f.writelines(content)
# #write a program to count total number of letters,digits and spaces in a file
# f=open('k.txt','r')
# content=f.read() #string format
# l_count=0
# d_count=0
# s_count=0
# for i in content:
#     if(i.isalpha()):
#         l_count+=1
#     elif(i.isdigit()):
#         d_count+=1
#     elif(i.isspace()):
#         s_count+=1
#     else:
#         pass
# print("letter count",l_count)
# print("space count",s_count)
# print('digit count',d_count)



# f=open('k.txt','r')
# content=f.readlines()
# content.reverse()
# print(content)
# f=open('k.txt','w')
# f.writelines(content)

# f=open('k.txt','a+') #writing content to the last position
# f.write('python')
#
# print(f.tell())           #returns the current file pointer position
# f.seek(0,0) ##seek(offset,from)
#                           ##changes the file pointer to the beginning
# content=f.read()
# # print(content)
# import os
# os.remove('k.txt')
# print("File is deleted")










