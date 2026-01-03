#Given a string
s="Hello world"
ch=input("Enter character")

if ch in s:
        print("Count of Character",ch,"is",s.count(ch))
else:
        print("Character",ch,"is not found")
# find the count of a particular character in a string

#
# #Given a string
# s="hello world"
# find the position of a particular character in a string
#
s="Hello world"
ch=input("Enter character")
if ch in s:
        print("Position of Character",ch,"is",s.index(ch))
else:
        print("Character",ch,"is not found")
#
# #Given a string
s="python coding is easy and fun"

d={}
for i in s:
    # if(i==" "):
    #     continue
    if i!=" ":
        d[i]=s.count(i)

print(d)

# create a dictionary where keys are characters and values are the count of characters


#
# #Given a string
s="python coding is easy and fun"
words=s.split()
for i in words:
    if(len(i)<5):
        print(i)
# print words whose length is less than 5
