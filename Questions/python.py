

#  =============================================revision 1                                                                                                                                    What do you mean by context?

# 1.features of python?
# high level,general purpose,multiprograming paragigm support,interactive, interpreted,dynamically typed,easy to learn, large community support large library suppoert
# 2.datatypes of python? ex:
# is the type of data that stored in variable:
#     numeric=
#            integer a=5 float a=5.6 complex 2+3j
#     text= collection of characters
#            string a="hello"
#     sequence
#               collection of hectrogenious type of elements
#             list,tuple
#          list  a=[1,3,4]
#          tuple a=(1,3,4)
#
#     mapping= dictionary  is a collection of key and value pair
#               a={'name':ram,'age':20}
#     set type=set      is collection of different elements unodered,no duplicates, only immutable
#               {1,2,3}
#     none
#     boolean
#
# 3.how to add new element in list,set and dictionary
#
# list: append() for 1 element add   ,   extend() for more element add
#
# set add : add() for 1 element add   ,       update() for more element add
# dictionary: using assignment operator = ,
#                              update(): Updates the dictionary with key-value pairs from another dictionary or iterable.
# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3
#
# my_dict = {'a': 1}
#
# my_dict.update({'b': 2, 'c': 3})
# # my_dict is now {'a': 1, 'b': 2, 'c': 3}
#
# 4. differance b/w mutable and immutable dt
#
# that mutable data types can be changed after they are created, while immutable data types cannot changed after creation
#     mutable : list,dict,set
#     immutable:tuple,numeric,string


#  =============================================revision 2                                                                                                                                      What do you mean by context?

# 1.What is slicing in Python?
# is a powerful operation that allows you to extract a specific portion or subset of a sequence (such as a string, list, or tuple).
# It is performed using the slice operator [] with colon-separated indices in the format [start:stop:step]


# 2.What is membership operator in Python? Explain with example?

#  used to test whether a value (or variable) is found within a sequence, such as a string, a list, a tuple, or a set. They return a Boolean value (True or False) based on the result of the check.
# There are two main membership operators in Python:
# in: Returns True if the value is present in the sequence, and False otherwise.
# not in: Returns True if the value is not present in the sequence, and False otherwise (the opposite of in).
# fruits = ["apple", "banana", "cherry"]
#
# # Check if "banana" is in the list
# print("banana" in fruits)  # Output: True


# 3.What is the difference between == and is operator in Python? Explain with example?

# The primary difference between Python's == and is operators lies in what they
# compare: == compares the values of two objects, while is compares their identity (whether they are the exact same object in memory).
# == (Equality Operator)
# The == operator checks if two objects have the same value. It evaluates whether the contents of the objects are equal.



# # 4.what are the different loop control statements in python?

# break: This statement terminates the current loop entirely and execution
# resumes at the next statement immediately following the loop [1]. It is commonly used when an external condition is met that warrants exiting the loop prematurely.
# continue: This statement skips the rest of the code inside the current loop iteration a
# nd proceeds immediately to the next iteration of the loop [1]. It is useful for skipping specific cases or erroneous data within a loop without terminating the entire process.
# pass: This is a null operation; nothing happens when it executes [1]. It is used as a placeholder where a statement is syntactically required but the programmer does not need
# any action or code to execute. This is useful for defining empty loops, functions, or classes
The pass statement is a null operation; it does nothing when executed. It's useful as a placeholder for code that you plan to write in the future.

# Using pass as a placeholder
for i in range(5):
    if i == 3:
        pass
    print(i)

#  =============================================revision 3                                                                                                                                      What do you mean by context?

# 1.What is lambda function.where we use lambda function
# A lambda function is a small, anonymous function defined without a name, typically used for short,
# one-time operations. They can take any number of arguments
# but can only have a single expression, the result of which is implicitly returned.
#Higher-Order Functions: Lambdas are commonly passed as arguments to functions that take other functions as input, such as:
map(): Applies a lambda function to every item in an iterable.
filter(): Uses a lambda function to select items from an iterable that satisfy a specific condition.
reduce(): Applies  computation to sequential pairs of values in an iterable and return single value of result
(requires importing from functools in Python).

# 2.what is decorator.explain with example
A decorator is a function or class that modifies or extends the behavior of another function or class
without changing its source code. It essentially "wraps" the original code,
adding extra functionality before, after, or around the original execution.

syntax:@decorator_name
it placed aboue the fuction defenision ,want to decore
decorator functions application area is authentication and autherization, which used to
restrict the access to specific function based on permission
@login_required example

# 3.what is comprehension.different types
Python comprehension is a concise and efficient way to create new sequences (lists, sets, dictionaries, or generators)
from existing iterables using a single, readable line of code

List Comprehension: Creates a new list. It is enclosed in square brackets [].
Syntax: [expression for item in iterable if condition]
Example:
python
squares = [x*x for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Set Comprehension:
Dictionary Comprehension:

#  =============================================revision 4                                                                                                                                    What do you mean by context?

# 
# #
# # What do you mean by *args and **kwargs?
# *args and **kwargs are special Python keywords used to pass a variable number
# of arguments to a function.
# *args collects positional arguments into a tuple,
# while **kwargs collects any keyword arguments into a dictionary.
# # They are useful when a function's number of arguments is not known in advance,
# # allowing for more flexible and reusable code.
# 
# #
# # What do you mean by a scope?what are the different types of scopes available in python?
# A scope in Python defines the region of a program where a variable or a name is recognized and can be accessed.
# It determines the visibility and lifetime of identifiers (like variable names, function names, class names, etc.) [1]. The scope ensures
# that variables declared within a function, for example, do not interfere with variables outside that function, even
# 
# Different Types of Scopes in Python
# Local (L) Scope:
# This is the innermost scope.
# Variables defined here are local to the specific function they are created within [1, 2].
# They only exist while the function is executing [1].
# Enclosing (E) Scope:
# This scope exists in nested functions (functions inside other functions) [1, 2].
# If a variable is not found in the Local scope, Python looks in the Enclosing scope (the outer function's scope) [1].
# Global (G) Scope:
# Variables defined here are at the top level of a script or module (outside of any function or class) [1, 2].
# They are accessible from anywhere within that module [1]. The global keyword is used to modify a global variable from within a local scope [2].
# Built-in (B) Scope:
# This is the broadest scope, containing all the pre-defined names built into Python itself, such as function names like print(), len(), str(), and exceptions like NameError [1, 2].
# 
# 
# Pickling and Unpickling in python?
# 
# pickling is the process of converting a Python object hierarchy into a byte stream (serialization),
# and unpickling is the inverse operation, converting the byte
# stream back into the original object hierarchy (deserialization). This is done using th
# e built-in pickle module.
# Pickling is the Python term for serializing an object, which entails transforming
# it into a binary representation that can be stored in a file or communicated over a network.
# Python has built-in functions for the pickling objects in the pickle module.
# In Python, deserializing a pickled object entails turning it from its  representation back to a Python object that can be used in code. This process is known as unpickling. Python's built-in pickle module has functions for unpickling objects.



#  =============================================revision 5                                                                                                                                      What do you mean by context?
#  What are OOPs Principles
#
# OOP principles (Object-Oriented Programming)
# are core concepts—Abstraction, Encapsulation, Inheritance, and Polymorphism
# class
# object
# Abstraction: Hiding complex implementation details and showing only essential features. Think of driving a car: you use the steering wheel and pedals without needing to know the engine's internal workings.
# Encapsulation: Bundling data (attributes) and methods (functions) that operate on the data within a single unit
#  and restricting direct access to some components. This protects data integrity.
# Inheritance: A mechanism where a new class (child/subclass) derives properties and behaviors from an existing class (parent/superclass),
# promoting code reuse and creating a hierarchy (e.g., a Dog class inheriting from an Animal class).
# Polymorphism: "Many forms." Allows objects to take on different forms or for a single interface

#
#  What is the Purpose of _init_ function
# It automatically perform when an object is created.in this,Python initializes a new class instance
#     by assigning values to its attributes
#    Its main purpose is to define the initial state and properties of an object.
# Purpose of __init__
# Object Initialization: Assigns initial values to object properties (attributes/variables).
# Automatic Execution: Runs automatically immediately after a new instance (object) of a class is created.
# Constructor Role: Serves as the equivalent of a constructor in other object-oriented languages like Java or C++.

#
# What is self keyword?                                                                                                                                                                                                                                                                what is the latest version of Python
# In Python, self is the first parameter in instance methods;
# it is not a reserved keyword. Its purpose is to refer to the specific instance (object) of the class
# on which a method is being called.
# Purpose and Function
# Access Instance Variables/Methods: This allows to maintain its own state independently for each object .
# Explicit Reference:  The name self makes it clear that the method is operating on the instance's data.
# Differentiation: It helps to distinguish between instance attributes (e.g., self.name) and local variables within a method.


#  =============================================revision 5                                                                                                                                      What do you mean by context?
#
# What is exception?How exception is handled in python
# An exception is an event that occurs during the execution of a program that disrupts its normal flow.
# In Python, exceptions are runtime errors , if it not handled,
# they cause the program to terminate abruptly.

# Python provides a structured mechanism to handle exceptions.
# try, except, else, and finally.
# the TRY block, which contains the code that might raise an exception,
# and the EXCEPT block, which contains the code to handle the exception if it occurs.
#
# ELSE block can be included after except blocks.
# Code in the else block runs only if the try block completes without raising any exceptions.
#
# The FINALLY block, executes in all cases – whether an exception occurred, was handled, or not. It's typically used for cleanup operations, like closing files.
#
#
# What is the difference between shallow copy and deep copy
# Shallow copy duplicates an object's top-level properties but shares references to nested objects,'
#  while a deep copy creates a completely independent copy of the object and all its nested objects.'
#  ' This means changes to nested objects in a shallow copy will affect the original, '
#  'but changes in a deep copy will not. Deep copies are slower and consume more memory, '
#  'whereas shallow copies are faster and more memory-efficient. ))
 
 


# What is re module in python?What are the different functions in re module
# The re module in Python provides support for regular expressions (regex),
# which are a powerful tool for pattern matching and manipulation of strings [1, 2]. Regular expressions are used to
# search for specific character sequences within a string, validate text formats, or perform text substitutions.
# used functions are re.match(),re.search(),re.findall(),re.finditer(),re.sub(),re.split()

#=========================== revision 8
# What is the difference between module and a package?.What is the use of import statement?
# A module is a single Python file (.py) containing code (functions, classes, variables),
# while a package is a directory that organizes related modules and sub-packages,
# identified by the presence of an __init__.py file  and the import statement is the mechanism used to access them.

# ==revision 9

# access specifier
#        access specifiers are used to control the accessibility of a variables and method of a class.
# python have no stritch specifiers like java and c++

#    public access specifier : member	Accessible from anywhere in the program.
#    protected: Accessible only within the defining class , denoted by _
#    private: Accessible within class and subclasses , denoted by __
