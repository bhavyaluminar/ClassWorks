# Create a database file school.db
#
# create a table Student with fields roll_no(pk),name,age,gender,course,mark
#
# write a menu driven code
#
#                     1.Insert Student details
#                     2.Read all student details
#                     3.search a student by rollno
#                     4.update the mark of a student
#                     5.Delete a student record
#                     6.Exit


import mysql.connector

con=mysql.connector.connect(user='root',password='root',host='localhost')
c=con.cursor()
c.execute('create database if not exists school')
print("created db file")

con=mysql.connector.connect(user='root',password='root',host='localhost',database="school")
cur=con.cursor()
cur.execute('create table if not exists student(roll_no int primary key,name varchar(30),age int,gender varchar(20),course varchar(20),mark int)')
print('created table')


def insert_record():
    r=int(input('Enter your roll_no:'))
    n=input('Enter your name:')
    a=int(input('Enter your age:'))
    g=input('Enter your gender:')
    c=input('Enter your course:')
    m=int(input('Enter your marks:'))

    cur.execute('insert into student(roll_no,name,age,gender,course,mark) values(%s,%s,%s,%s,%s,%s)',(r,n,a,g,c,m))
    con.commit()
    print('Student data inserted')

while(True):
    print('1.Insert')
    print('2.Read')
    print('3.Search')
    print('4.Update')
    print('5.Delete')
    print('6.Exit')

    ch=int(input('Enter your choice:'))
    if ch==1:
        insert_record()
    elif ch==2:
        pass
    elif ch==3:
        pass
    elif ch==4:
        pass
    elif ch==5:
        pass
    else:
        exit()


