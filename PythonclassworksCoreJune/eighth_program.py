#write a program to interchange(swap) the values of two variables
#1.using a 3rd variable
a=3
b=5

temp=a  #temp =3
a=b     #a =5
b=temp  #b =3
print(a,b)


#2.without using 3rd variable

a=3
b=5
a,b=b,a

print(a,b)