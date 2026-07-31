#find the number of lines in a file


#find the number of words in a file


#program to display last 5 lines in a file


# #program to change the content of second line in a file

# #progran to search a particular word inside the file


# #find the number of letters,digits and spaces inside the file.



#reverse the lines in a file

# A file total_students.txt contains the names of all students in a class,
# and a file passed_students.txt contains the names of students who passed the exam.
# Write a Python program to:
# Read the names from both files.
# Find the students who did not pass.
# Write their names to a new file named failed_students.txt, one name per line.

f1=open('total.txt','r')
l1=f1.readlines()
print(l1)

f2=open('pass.txt','r')
l2=f2.readlines()
print(l2)

f3=open('fail.txt','w')
for i in l1:
    if i not in l2:
        f3.write(i)
f1.close()
f2.close()
f3.close()




# Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it.

f1=open('swiggy.txt','r')
l1=f1.read().split()
print(l1)

f2=open('zomato.txt','r')
l2=f2.read().split()
print(l2)
l=l1+l2
print(l)

d={}
for i in l:
    d[i]=l.count(i)
print(d)






# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt.

f1=open('marks.txt','r')
l=f1.readlines()
# print(l)

f2=open('names.txt','w')
for i in l:

    r=i.split()
    print(r)
    if(int(r[1])>75):
        f2.write(r[0]+'\n')

