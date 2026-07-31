# # 1.Create a table named students to store student information.
# # Table: students
# # Column Name
# # Data Type
# # Description
# #
# # student_id
# # INT (Primary Key)
# # Unique student ID
# #
# # name
# # VARCHAR(100)
# # Name of the student
# #
# # age
# # INT
# # Age of the student
# #
# # gender
# # VARCHAR(10)
# # Gender
# #
# # course
# # VARCHAR(100)
# # Enrolled course
# #
# # marks
# # INT
# # Marks obtained
# #
# # city
# # VARCHAR(100)
# # City of the student
# #
# #
# # Questions
# # Display all records from the students table.
#   select  * from students
# # Display name, course, and marks for all students.
# select name,course,marks from students
# # Display names and marks of students who scored more than 80.
# select name,marks from students where marks>80
# # Display all details of students enrolled in Computer Science.
# select * from students where course="computerscience"
# # Display names, ages, and cities of students whose age is between 18 and 22.
# select name,age,city from students where age between 18 and 22
# # # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.
# # select name,marks,course from students where city="kochi" order by marks desc
# # # Count the total number of students in each city.
# # select city,count(*) from students group by city
# # # Display the average marks obtained by students in each course.
# # select course,avg(marks) from students group by course
# # # Display details of the student(s) with the highest marks.
# # select * from students where marks=(select max(marks) from students)
# #
# # # select * from students order by marks desc limit 1
# # # Insert a new record into the students table.
# #
# # # Update marks of all students who scored below 50 by adding 5 bonus marks.
# # update students set marks=marks+5 where marks<50
# # # Delete all student records where marks are less than 35.
# # delete from students where marks<35;
# #
# # 2.Create 2 tables departments and employees
# # Table: departments
# # Column Name
# # Description
# #
# # id
# # Department ID (Primary Key)
# #
# # department_name
# # Name of the department
# #
# #
# # Table: employees
# # Column Name
# # Description
# #
# # id
# # Employee ID (Primary Key)
# #
# # employee_name
# # Name of the employee
# #
# # age
# # Age of the employee
# #
# # salary
# # Salary of the employee
# #
# # joining_year
# # Year the employee joined
# #
# # department_id
# # Department ID (Foreign Key)
# #
# # city
# # Employee city
# #
# #
# #
# # Questions
# # Retrieve all records from the departments table.
# select * departments;
# # Retrieve employee_name, age, and salary from the employees table.
# select employee_name,age,salary from employees
# # Retrieve employee_name and salary for employees earning more than 50000.
# select employee_name,salary from employees where salary >50000
# # Retrieve employee_name, age, and city for employees whose name contains “John”.
# select employee_name,age,city from employees where employee_name like '%John%'
#
# # Retrieve employeename, salary, and joiningyear for employees who joined before 2020 and have salary greater than 60000.
# select employee_name,salary,joining_year from employees where joining_year<2020 and salary>60000
# # Retrieve employeename, city, and joiningyear for employees who joined after 2018, sorted by joining_year in ascending order
# select employee_name,city,joining_year from employees where joining_year>2018 order by joining_year
# # Find the number of employees in each city.
# select city,count(*) from employees group by city
# # Find the number of employees grouped by joiningyear and city, sorted by joiningyear.
#
# select joining_year,city,count(*)
# from employees group by joining_yeat,city order by joining_year
# # Find cities and their average salary, showing only cities where average salary is greater than 45000.
# sleect city,avg(salary) from employees group by city having avg(salary)>45000
#
# # Retrieve employee names along with their corresponding department names.
# select employee_name,department_name from employees inner join departments on employees.department_id=
#                                                                   departments.id
# (2hrs)
#
# #To delete a db table
#
# drop table tablename
#
# #to delete a db file
# drop database dbname;