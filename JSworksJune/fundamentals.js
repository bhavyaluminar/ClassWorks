
//multiplication table of a number entered by user(upto10)
// num=Number(prompt("Enter a number"))
//
// for(let i=1;i<=10;i++){
//     //console.log(num,"*",i,"=",num*i)
//     console.log(`${num}*${i}=${num*i}`)
// }
// //sum of first 10 even numbers(1,20)
//product of odd numbers in the range(1,50)


//for -of(sequence iteration -string/array)

// var s="hello";//string
//
// for(let i of s){
//     console.log(i)
// }
//
//
// var a=['red','green','blue']
//
// for(let i of a){
//     console.log(i)
// }


//for -in (Object iteration)

// var p={'name':'arun','age':23}
//
// for(let i in p){
//     console.log(i)//property
//     console.log(p[i])//value
// }
//


// Functions

// //function definition
// function functionaname(parameters)
// {
//     //statements
//     //return expression
//
// }
//
// //function call
// functionname(arguments)

//
// //without parametrs
// // function greet(){
// //     console.log('hello')
// // }
// //
// // greet()
//
//
// //with parameters
//
// function greet(n){
//     console.log(`hello ${n}`)
// }
//
// greet('Arun')
// greet('Amal')
//
//
// //With return statement
//
// function add(a,b){
//     s=a+b
//     return s
// }
//
// var sum=add(7,8)
// console.log(sum)
//


//define a function to print multiplication table of a number entered by
//user

//define a function that accepts a string and find the count of a
//specific character tn a string


//define a function to enter name 5 times.Each time print hello 'name'

//define a function to find the reverse of a string

//Write a function that allows 3 attempts to enter the correct password.
// if the user enters correct password at any attempt print "Login Successful"
// and stops the program.if all
// 3 attempts fail ,print "Account locked"

// function check_password(){
//     correct_password="admin123"
//     for(let i=1;i<=3;i++){
//         let password=prompt("Enter password")
//         if(password==correct_password){
//             console.log("Login successful")
//             return
//         }
//
//         if(i==3)
//         {
//             console.log("Account locked")
//
//         }
//
//
//     }
// }


// check_password()


//Arrow Function

    //(parameters)=>expression


// function greet(){
//     console.log("hello")
// }
//
// greet()
//
// const greet=()=>console.log("hello")
//
// greet()
// //With arguments
//
// const add=(a,b)=>(a+b)
//
// console.log(add(7,8))


//define arrow function to find the product of 3 numbers
// const p=(a,b,c)=>console.log(a*b*c)
// p(5,6,7)
// //define arrow function to find the square of a number
//     (n)=>console.log(n**2)
// //define arrow function to find the first element inside an array
//     (a)=>console.log(a[0])
// //define arrow function to find the length of the string
// //     (s)=>(s.length)
// // //define arrow function to print the name of an object
// //     (o)=>o['name']
//
// //Define a function to find count of  vowels in a string
//
// s="hello world"
//
// function count_vowels(s){
//     count=0;
//     vowels="aeiouAEIOU"
//     for(let i of s){
//         if(vowels.includes(i)){
//             count++;
//         }
//
//
//     }
//     console.log(count)
// }
//
// count_vowels(s)
//
//
//
//
//


// Map()
//
// array.sequence(function)
//
// Create a new array with length of each element
// c=['red','green','blue','orange']


//
// Create a new array with first character of each element
// c=['red','green','blue','orange']
//

// create a new array with salaries of each employee
// var e=
//     [{'name':'arun','salary':20000},
//     {'name':'amal','salary':30000}
// ]
//
// create a new array with names of each employee
// var e=[{'name':'arun','salary':20000},
//     {'name':'amal','salary':30000}
// ]
//
// Add 5000 to each employee salary
// var e=[{'name':'arun','salary':20000},
//     {'name':'amal','salary':30000}
// ]



// Filter

// array.filter(function)

var a =[23,67,12,90,46]

//even values
// console.log(a.filter(i=>i%2==0))

//
// var b=[34,67,-13,89,-34,67]
//
// //positive even values
// // console.log(b.filter(i=>i>0 && i%2==0))
// //
//
// // Reduce
//
// var a=[1,2,3,4]
//
// //sum of array
// console.log(a.reduce((x,y)=>x+y,0))
//
// //product of array
// console.log(a.reduce((x,y)=>x*y,1))
//
// //
//
// var p= [{'name':'laptop','price':50000},
//     {'name':'phone','price':20000},
//     {'name':'watch','price':3000},
//     {'name':'Tablet','price':25000}]
//
// //print array of product names in Uppercase
// console.log(p.map(i=>i.name.toUpperCase()))
//
// //print products with price greater than 10000
// console.log(p.filter(i=>i.price>10000))
//
// //Find the total price of all products
// console.log(p.reduce((i,j)=>i+j.price,0))


// Object

//entries
//keys
//values

//Object.entries(objectname)
//Object.keys(objectname)
//Object.values(objectname)



//Spread Syntax

//to create independent copy of an object/array

// [...arrayname]
// {...objectname}





















//for of
//for in


















































//using class syntax














