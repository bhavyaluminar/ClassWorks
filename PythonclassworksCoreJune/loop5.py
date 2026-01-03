# Q1.
d={101:['Arun',23,'ekm'],
     102:['Amal',25,'tvm'],
     103:['Anu',26,'tcr'],
      104:['Kiran',27,'ekm']}

#print all names of students
for i in d.values():
    print(i[0])
#print the average age
sum=0
average=0
for i in d.values():
    sum=sum+i[1]
average=sum/len(d)
print(average)
#print student details whose place is ekm
for i in d.values():
      if(i[2]=="ekm"):
            print(i)



#Q2.sum of numbers in the range(100,200)
sum=0
for i in range(100,201):
    sum=sum+i
print(sum)
#Q3.print the characters at even index position
s="hello world"

# for  i in s:
#     print(i)

#even values
for i in range(0,len(s),2):
    print(s[i])








