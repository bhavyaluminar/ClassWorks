import sqlite3

con=sqlite3.connect("company.db")
      #if file exists it returns reference to con
      #else it creates a new db file and returns its reference to con

#print("Database file created")

command="""create table if not exists employee(empid int primary key NOT NULL,
name varchar(20),age int,salary int,designation varchar(20),gender varchar(10),place varchar(20))"""

con.execute(command)
# print("Table created")


# con.execute("""
# insert into employee (empid,name,age,salary,designation,gender,place)
# values(101,"Arun",23,30000,"Developer","male","ekm"),
# (102,"Amal",24,40000,"Sales","male","tvm"),
# (103,"Anu",30,50000,"Developer","female","ekm")""")

# con.execute('''insert into employee(empid,name,age,salary,designation,gender,place)
# values('',"Arun",23,30000,"Developer","male","ekm")''')
# con.commit() #to save data permanently
# print("Inserted data successfully")

#READ OPERATION
#all employee records(with all attributes)
# k=con.execute('select * from employee')
# print(k.fetchall())
#
# #specific employee records(with all attributes)
# k=con.execute('select * from employee where empid=101')
# print(k.fetchall())
#
#
# #specific employee records(with specific attributes)
# k=con.execute('select empid,name,age from employee where empid=101')
# print(k.fetchall())


# =,!=,<,>,<=,>=,and,or,not,like,between,in

#and
#employee having age=23 and salary>20000

# k=con.execute('select * from employee where age=23 and salary>20000')
# print(k.fetchall())

# #employee records having age other than 23
# k=con.execute('select * from employee where not(age=23)')
# print(k.fetchall())


#LIKE

# % --0 or more characters
# _ --exactly one character

#Employees having name starting with letter 'A'
# k=con.execute('select * from employee where name like "A%"')
# print(k.fetchall())
#
# #employees having 3 letter name starting with 'A'
# k=con.execute('select * from employee where name like "A__"')
# print(k.fetchall())
#
# #employees having name contains letter 'r'
# k=con.execute('select * from employee where name like "%r%"')
# print(k.fetchall())


#between

#emplyees having salary between 15000 and 30000(including 15000 and 30000)

# k=con.execute("select * from employee where salary between 15000 and 30000")
# print(k.fetchall())


#in

#employees with age=23 or age=30

# k=con.execute("select * from employee where age in (23,30)")
# print(k.fetchall())


#read first row

#read first 2 rows

#read 1 row after skipping 2 rows

#read 2 rows after skipping 2 rows


#Order by
# k=con.execute("select * from employee")
# print(k.fetchall())
#
# k=con.execute("select * from employee order by salary")
# print(k.fetchall())
#
#
# k=con.execute("select * from employee order by age desc;")
# print(k.fetchall())


con.execute('update employee set age=28 where empid=103')

#con.commit()
k=con.execute('select * from employee')
print(k.fetchall())

# empid,name,age,salary,designation,gender,place)
# con.execute('insert into employee values(105,"akhil",26,25000,"developer","male","ekm")')
#
# k=con.execute("select * from employee")
# print(k.fetchall())


#Delete

con.execute('delete from employee where empid=102')
con.commit()
k=con.execute("select * from employee")
print(k.fetchall())





































