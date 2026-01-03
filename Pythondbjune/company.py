import sqlite3

con=sqlite3.connect("company.db")  # if db file already exists it returns connection reference to con
                                   #else it will create an empty db file and returns reference to con

# #Create table tablename(field1 type1,field2 type2,.............)
#
# # sql_command="create table employee(empid int primary key,name varchar(20),age int,gender varchar(10),salary int,place varchar(20))"
# #
# # # con.execute(sql_command) #creates a table inside db file
# # # print("Table Created")
# #
# # #insert into tablename(field1,field2,.........)values(value1,value2,......)
# #
# # #
# # # # con.execute("insert into employee(empid,name,age,gender,salary,place)values(100,'Arun',23,'male',20000,'ekm')")
# # # con.execute("insert into employee(empid,name,age,gender,salary,place)values(101,'Amal',25,'male',25000,'tvm')")
# # # con.execute("insert into employee(empid,name,age,gender,salary,place)values(102,'Anu',23,'female',30000,'kollam')")
# # # con.execute("insert into employee(empid,name,age,gender,salary,place)values(103,'kiran',27,'male',27000,'tcr')")
# # # con.execute("insert into employee(empid,name,age,gender,salary,place)values(104,'manu',30,'male',35000,'tvm')")
# # # con.commit() #to store records permanently in db file
# #
# # #Read Operation
# #
# # #All records(with all attributes)
# # k=con.execute('select * from employee')
# # print(k.fetchall())
# #
# # #All records(with specific attribute)
# # k=con.execute('select name,age from employee')
# # print(k.fetchall())
# #
# # #Specific record(with specific attributes)
# # k=con.execute('select name,age from employee where empid=100')
# # print(k.fetchall())
# #
# # #Specific record(with all attributes)
# # k=con.execute('select * from employee where empid=100')
# # print(k.fetchall())
# #
# # #specific records(with all attributes)
# # k=con.execute('select name,age from employee where place="ekm"')
# # print(k.fetchall())
#
# #LIMIT AND OFFSET
# #read first row
# # k=con.execute('select * from employee limit 1')
# # print(k.fetchall())
# # #read first two rows
# # k=con.execute('select * from employee limit 2')
# # print(k.fetchall())
# # #read one row after skipping first row
# # k=con.execute('select * from employee limit 1 offset 1')
# # print(k.fetchall())
# #
# # #read two rows after skipping first two rows
# # k=con.execute('select * from employee limit 2 offset 2')
# # print(k.fetchall())
#
# #=,!=,<,>,<=,>=,and,or,not,like,between,in,distict,orderby
#
# #records having empid other than 102
# # k=con.execute('select * from employee where empid!=102')
# # print(k.fetchall())
#
# #records having age value less than 27
# # k=con.execute('select * from employee where age<27')
# # print(k.fetchall())
#
# #records having salary>25000
# # k=con.execute('select * from employee where salary>25000')
# # print(k.fetchall())
#
# #records having age<27 or place="ekm"
# # # k=con.execute('select * from employee where age<27 or place="ekm"')
# # # print(k.fetchall())
# #
# # # records having age value other than 27
# # # k=con.execute('select * from employee where not(age=27)')
# # # print(k.fetchall())
# #
# # #between
# # # records having age between 27 and 35(including 27 and 35)
# # k=con.execute('select * from employee where age between 27 and 35')
# # print(k.fetchall())
# #
# # #records having salary between 20000 and 30000
# # k=con.execute('select * from employee where salary between 20000 and 30000')
# # print(k.fetchall())
# # #
# # #
# # # #records with salary 20000 or 30000
# # # k=con.execute('select * from employee where salary in(20000,30000)')
# # # print(k.fetchall())
# # #
# # # #records with salary other than 20000 and 30000
# # # k=con.execute('select * from employee where salary not in(20000,30000)')
# # # print(k.fetchall())
# #
# # #Like
# # #
# # # % -->0 or more characters
# # # _ -->exactly one character
# #
# #
# # #3 letter name ending with u
# # k=con.execute('select * from employee where name like "__u"')
# # print(k.fetchall())
# # #name ending with u
# # k=con.execute('select * from employee where name like "%u"')
# # print(k.fetchall())
# #
# # #4letter name starting with 'a'
# # k=con.execute('select * from employee where name like "a___"')
# # print(k.fetchall())
# #
# # #place name starting with letter 'k'
# # k=con.execute('select * from employee where place like "k%"')
# # print(k.fetchall())
# #
# # #name contains letter 'n'
# # k=con.execute('select * from employee where name like "%n%"')
# # print(k.fetchall())
#
# #Order By
#
# #read records based on name(in ascending order)
# k=con.execute('select * from employee order by name')
# print(k.fetchall())
#
# #read records based on salary (in ascending order)
# k=con.execute('select * from employee order by salary')
# print(k.fetchall())
#
# #read records based on salary (in descending order)
# k=con.execute('select * from employee order by salary desc')
# print(k.fetchall())
#
# #Distinct
# k=con.execute('select distinct(place) from employee')
# print(k.fetchall())


#Update Operation

# print("Before Updation")
# k=con.execute('select * from employee')
# print(k.fetchall())
#
# con.execute('update employee set age=28,salary=40000 where  empid=101')
# con.commit()
#
# print("After Updation")
# k=con.execute('select * from employee')
# print(k.fetchall())

#Delete Operation
#
# print("Before Deletion")
# k=con.execute('select * from employee')
# print(k.fetchall())
#
# con.execute('delete from employee where empid=102')
# con.commit()
#
# print("After Deletion")
# k=con.execute('select * from employee')
# print(k.fetchall())

#Alter command

#To add new column email
#
# con.execute('alter table employee add column email varchar(30)')
#
# k=con.execute('select * from employee')
#
# print(k.fetchall())
#
# #to remove column
#
# # con.execute('alter table employee drop column email')

#To rename tablename

# # con.execute('alter table employee rename to employee1')
#
# k=con.execute('select * from employee1')
# print(k.fetchall())

#To rename column name
# con.execute('alter table employee1 rename column empid to id')

#Aggregate Functions
# k=con.execute('select sum(salary),min(age),max(age),count(*),avg(salary) from employee1')
# print(k.fetchall())


# k=con.execute('select sum(salary) from employee1')
# print(k.fetchall())
#Group by -Having
# k=con.execute('select place,sum(salary) from employee1 group by place')
# print(k.fetchall())

# con.execute('''insert into employee1 values(105,"ammu",25,"female",37000,"tcr"),
#                                            (106,"minu",25,"female",42000,"tvm")''')
# con.commit()

k=con.execute('select gender,max(age) from employee1 group by gender')
print(k.fetchall())








































































