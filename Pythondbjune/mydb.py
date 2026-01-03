import mysql.connector


# con=mysql.connector.connect(user="root",password="root",host="localhost")
#                             #establish connection to the mysql db server
#                             #returns connection reference to con
# print(con)
#
# c=con.cursor()  #cursor object -to execute sql queries in mysql
#
# c.execute("create database mydb") #creates a db file inside database server
#
# print("Database file created")


con=mysql.connector.connect(user="root",password="root",host="localhost",database="company")
c=con.cursor()
# c.execute("""create table employee
#              (empid int primary key,
#              name varchar(20),age int,
#              place varchar(20),
#              salary int,
#              gender varchar(10))""")
# print("Table created")

# c.execute('''insert into employee values(100,"arun",23,"ekm",30000,"male"),
#                                       (101,"amal",25,"tvm",35000,"male"),
#                                       (102,"anu",27,"ekm",45000,"female"),
#                                        (103,"kiran",29,"kollam",50000,"male"),
#                                        (104,"minu",24,"tcr",30000,"female"),
#                                        (105,"manu",26,"tvm",40000,"male")''')
# print("inserted data")
# con.commit() #to save data permanently
#
#
#
# c.execute('select * from employee')
# k=c.fetchall()
# print(k)











