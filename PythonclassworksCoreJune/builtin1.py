# # #Given a list
# #
# # l=[1,1,2,2,2,3,5,6,6,7]
# # # d={}
# # # for i in l:
# # #     d[i]=l.count(i)
# # # print(d)
# # # create a new dictionary where keys are numbers and values are count of ech number
# # # # #Given two lists
# #
# # # #1
# # l1=[10,24,67,13,90]
# # l2=[24,78,90,11]
# # # # find the common elements
# # # s1=set(l1)
# # # s2=set(l2)
# # # print(list(s1.intersection(s2)))
# #
# # #2
# # for i in l1:
# #     if i in l2:
# #         print(i)
#
#
# #
# # #Given a list
# l=[10,24,67,13,90]
# # Find the largest value
# # print("Largest value",max(l))
#
# max=l[0]
# for i in l:
#     if(i>max):
#         max=i
#
# print(max)
# # #Given a list
# l=[10,24,67,13,90]
# # Find the smallest value
# # print("smallest value",min(l))
# min=l[0]
# for i in l:
#     if(i<min):
#         min=i
#
# print(min)
#
# #Given a list
# l=[10,24,67,13,90]
# l.sort()
# print(l[1])
# # Find the second smallest value
# #
# #
# # # #Given a list
# l=[10,24,67,13,90]
# # # Find the second largest value
# l.sort()
# print(l[-2])
#
# #
# # #given a list
# l=[['arun',23,30000],['amal',26,40000],['anu',27,50000]]
# #max(seq)
# # #l-->[30000,40000,50000]
# new=[]
# for i in l:
#     new.append(i[2])
# print(max(new))
#find the highest salary

s="python is a programming abcdefghijk language"
# find the maximum length word from the string

words=s.split() #split the string into words

max_length=max([len(i) for i in words]) #find the maximum lenggth

for i in words:
    if len(i)==max_length:
        print(i)
        break




