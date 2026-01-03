import mysql.connector
con=mysql.connector.connect(user="root",password="root",host="localhost")
c=con.cursor()
c.execute("create database shop")
print("Database file created")
con=mysql.connector.connect(user="root",password="root",host="localhost",database="shop")
c=con.cursor()
c.execute("create table product (pid int primary key,pname varchar(20),price int)")
print("Table product created")

c.execute("create table order_details (orderid int primary key,pid int,order_date date,quantity int,foreign key (pid) references product(pid))")
print("Table order_details created")

c.execute("insert into product values(1,'productA',200),(2,'productB',500),(3,'productC',1000),(4,'productD',550)")
print("Data inserted")
con.commit()

c.execute("insert into order_details values(100301,3,'2025-03-20',1),(100302,2,'2025-06-25',2)")
print("Data inserted")
con.commit()