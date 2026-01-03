// JAVASCRIPT SYNTAX
//
// comment
//
// // --single line
// /*  ...multiline..*/

//variables
       // var/let/const
// var x=10;  //global scope
// let x=10;  //block level scope
// const x=10; //constant cannot be changed

// for(const x=1;x<=5;x++){
// console.log(x);
// }
//  console.log(x)
// //Datatypes
//primitive
//      //int
//     //float
//     //string
//     //boolean
//    //null
//    //undefined
//
// var companyName="Luminar Technolab" //string
// var noOfEmployees=120;  //int
// var rating=5.0;//float
// var isOpen=true;  //boolean
//
// console.log("companyName:",companyName);
// console.log("Number of Employees:",noOfEmployees);
// console.log("companyName:",rating);
// console.log("companyName:",isOpen);
// console.log("companyName:",typeof(companyName));
// console.log("Number of Employees:",typeof(noOfEmployees));
// console.log("companyName:",typeof(rating));
// console.log("companyName:",typeof(isOpen));
//
//
// var x=null;//no value/empty value;


// var y;     //no value is assigned
// console.log(y);  //undefined type


//non primitive types
// Arrays
// Objects

// //array
// var a=[10,20,30,40]
// console.log(a,typeof(a))
//
// console.log(a[0],a[1],a[2],a[3])
//
//
// //object
// var person={
//         'name':'arun','age':20
// }
//
// console.log(person,typeof(person))
// console.log(person.name,person['name'])
// console.log(person.age,person['age'])

//Operators

// Arithemetic ->[+,-,/,%,*,**,++,--]
// Relational ->[<,>,<=,>=,==,!=]
// Assignment ->[=,+=,-=,*=,/=]
// Logical ->[&&,||,!]
// && -and
// || -or
// ! -not
//
// var a=20;
// a--;
// console.log(a)

//
// // conditional statement
//
// // if -else
// // if -elseif -else
//
// if(condition) {
//     //stmts to execute if condition true
// }
// else {
//     //stmts to execute if condition false
// }
//
//
//
// if(condition1) {
//     //stmts to execute if condition1 true
// }
// else if(condition2)
// {
//     //stmts to execute if condition2 true
// }
// else {
//     //stmts to execute if all the above conditions are false
// }
//
// 1.
// fizzbuzz
//
// Given a number
//display Fizz if number is / by 3
//display Buzz if number is /by 5
//display FIZZBUZZ if number is /15
//else display invalid number


// 2.
// //Given Height and Weight
//
// //display bmi


//Looping

////find the factorial
//var num=5;
//var f=1;
//for(var i=1;i<=num;i++)
//{
//f=f*i;
//}
//console.log(f)
////print the series (100-1)
//
//for(var i=100;i>=1;i--){
//console.log(i);
//}

//for -of(seq)
//
//var s="hello"; //string
//
//for(let i of s){
//console.log(i)
//}
//
//
//var colors=['red','green','blue'] //array
//
//for(let i of colors){
//console.log(i)
//}
//


//for -in (object)
//
//var obj={'name':'arun','age':24,'place':'ekm'}
//
//for (let i in obj){
//  console.log(i,obj[i])
//}

//write a program to find the reverse of a string
//var s="hello";
//var rev=""
//for(let i of s){
//   rev=i+rev
//
//}
//console.log(rev)
////find the sum of elements in an array
//var l=[23,12,56,47,89,11]
//var sum=0;
//for(let i of l){
//   sum=sum+i;
//}
//console.log(sum)
//find the sum of odd elements in an array
//var l=[23,12,56,47,89,11]
//
//var sum=0;
//for(let i of l){
//if(i%2!=0){
//sum=sum+i
//}
//
//}
//console.log(sum)

//find the characters at even index position

//var s="hello"
//
//for(let i=0;i<s.length;i++){
//if(i%2==0){
//
//console.log(s[i])
//}
//}
//
//var s="hello";
//for(let i=0;i<s.length;)
//{
//console.log(s[i])
//i=i+2;
//}


//FUNCTIONS

//function definition
//function functioname(parameters){
//  //function body
//    return [expression]
//}
//
////function call
//functionaname(arguments)
//
////
////function fact(n){
////
////    var f=1;
////    for(let i=1;i<=n;i++){
////        f=f*i;
////    }
////    console.log("Factorial is",f)
////}
////
////fact(5)
//
//
////define a function find the number of occurence of a character in a given string
//
//var s="Hello World"
//function count_character(s){
//var count=0;
//for (let i of s){
//   if(i=='l')
//   {
//   count++;
//   }
//}
//console.log(count)
//}
//
//
//
//count_character(s)
//
////define a function to find the factors of a number
////eg:
////if given number is 8
//////factors are -1,2,4,8
////
////var n=8;
////function factors(n){
////    for(let i=1;i<=n;i++){
////
////    if(n%i==0){
////
////    console.log(i)}
////    }
////}
////
////factors(n)
////
//
////Arrow function
//
//
////user defined
////
////function sum(a,b){
////   return a+b
////}
////
////
////console.log(sum(7,8))
//
////arrow function
//
//(parameters)=>{expression}
//
//var s=(a,b)=>a+b
//console.log(s(7,8))


//built in functions

/////String
var s="javascript"
//at
console.log(s.at(2))
console.log(s.at(-2))
//charAt
console.log(s.charAt(2))
console.log(s.charAt(-2))

//indexOf
console.log(s.indexOf('j'))

//startsWith()
console.log(s.startsWith('p'))

//endsWith()
console.log(s.endsWith('t'))

////repeat()
//console.log(s.repeat(3))
//console.log('*'.repeat(5))
//
////includes()
//console.log(s.includes('p'))
//console.log(s.includes('k'))
//
////slice(start,stop) //ascending order
//console.log(s.slice(2,7))//2,3,4,5,6
//
////split()
//console.log(s.split('a'))
//var k="javascript is a programming language"
//console.log(k.split(' '))
//
////toLowerCase
//console.log(s.toLowerCase())
////toUpperCase
//console.log(s.toUpperCase())
//
////to convert it into string type
////String()
//
////to convert it into number type
////Number()
//
//
////Array related Function
//var a=['red','green','blue']
////push() ##adds new element to the endposition
//a.push('black')
//console.log(a)
//
////pop() //removes from end position
//console.log(a.pop())
//
////shift() #remove elements from starting position
//console.log(a.shift())
//console.log(a)
//
//////unshift()  #add elements at the beginning(one or more element)
////a.unshift(2,3)
////console.log(a)
////
//////slice()
////console.log(a.slice(2,5))
////
//////reverse()
////console.log(a.reverse())
////
//////indexOf()
////console.log(a.indexOf('blue'))
////
//////splice(position,deletecount,element1,element2) /delete/add/replace
//
////write a program to find the count of vowels,consonants and digits in a string
//
//var s="aertyuio fghjkl 456789 fghjkl"
//var v_count=0;
//var c_count=0;
//var d_count=0;
//var vowels="aeiou"
////var consonants="bcdfghjklmnpqrstuvwxyz"
////var digits="0123456789"
//for(let ch of s){
//      if(vowels.includes(ch))
//         {
//            v_count++;
//           }
//     else if(ch>='a' && ch<='z'){
//      c_count++;
//      }
//      else if(ch>='0' && ch<='9'){
//       d_count++;
//      }
//      else{
//      }
//
//}
//console.log("vowels",v_count)
//console.log("digits",d_count)
//console.log("consonants",c_count)

//if(ch>='a' && ch<='z')


//Objects
var obj={'name':'arun','age':23}
//entries
console.log(Object.entries(obj))
//keys
console.log(Object.keys(obj))
//values
console.log(Object.values(obj))
































































































































































//operators
//conditional stmts
//looping
//functions
//higher order functions
//Arrow function
//SWITCH-CASE

//Switch -case

// //syntax
//
// switch(expression){
//
//     case value1:
//            #code to execute if value of expression matches with value1
//     break;
//
//     case value2:
//            #code to execute if value of expression matches with value2
//     break;
//     case value3:
//            #code to execute if value of expression matches with value3
//     break;
//
//     default:
//         default code
//         break;
// }
// var day=8;
//
// switch(day){
//
//     case 1:
//          console.log('sunday')
//          break;
//     case 2:
//         console.log('monday')
//         break;
//
//     case 3:
//         console.log('tuesday')
//         break;
//     default:
//         console.log('other day')
//         break
// }


//Looping statements

//while
//for
//do-while
//for -of(sequence/string/array iteration)
//for --in(object iteration)



// Syntax

//WHILE
// while(condition){
//     //stmts
// }
// //fOR
// for(initialization;condition;incrementation){
//     //stmts
// }
// //DO-WHILE
// do{
//     //stmts
// }
// while(condition);


//1,2,3,4,5
// var i=1;
// while(i<=5){
//     console.log(i)
//     i++;
// }


// for(var i=1;i<=5;i++){
//     console.log(i)
// }

// var i=1
// do {
//     console.log(i)
//     i++
// }while(i<=5)


// Spread Syntax  -To create a shallow copy/indepndent copy of array
 //[...arrayname]
//
// var a=[1,2,3,4]
// var a1=[...a]
// console.log(a)
// console.log(a1)
//
// a1.push(5)
//
// console.log(a)
// console.log(a1)
//

//spred syntax to create copy -{...objectname}
// var obj={'name':'arun','age':23}
// var obj1={...obj}
// console.log(obj)
// console.log(obj1)
//
// obj1['age']=30
// console.log(obj)
// console.log(obj1)




// var a=[1,2,3,4]
// var a1=[...a,5,6] //[1,2,3,4,5,6]
// console.log(a)
// console.log(a1)
//
// var obj={'name':'arun','age':23}
// var obj1={...obj,'place':'ekm'}
// console.log(obj)
// console.log(obj1)


//template Literal
//
// var name="amal";
// var age=23;
//
// console.log(`name is ${name} and age is ${age}`)


//class
//
// class classname{
//
//     ##attributes
//     #methods
//
// }
//Object creation through Class
class Student{
    constructor(n,a){
        this.name=n;
        this.age=a;
        }
    display(){

        console.log(this.name,this.age)
    }
}

var s=new Student('arun',23)
s.display()




//object declaraton through literal
// var s={'name':'arun',
//         'age':23,
//         display:function()
//                        {
//                        console.log(this.name,this.age)
//                        }
//        }


























