import mysql.connector
con=mysql.connector.connect(user="root",password="root",host="localhost",database="mydb")
c=con.cursor()
#
# c.execute('create table person(id int primary key,name varchar(20),age int)')
# print("Table created")

i=int(input("Enter the id"))
n=input("Enter name")
a=int(input("Enter age"))


c.execute('insert into person values(%s,%s,%s)',(i,n,a))
con.commit()

i=int(input("Enter the id"))
c.execute('select * from person where id=%s',(i,))
print(c.fetchall())