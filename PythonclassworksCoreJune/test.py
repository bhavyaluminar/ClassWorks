# 1 0 0 0 0
# 0 2 0 0 0
# 0 0 3 0 0
# 0 0 0 4 0
# 0 0 0 0 5

# for i in range(1,6):
#     for j in range(1,6):
#         if(i==j):
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()


s="madam and racecar are level racecar madam"
words=s.split()
d={}
for i in words:
    d[i]=len(i)
print(d)




