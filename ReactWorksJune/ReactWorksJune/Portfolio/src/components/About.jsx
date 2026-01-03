import React from 'react'


// JSX-Javascript+HTML(Javascript XML Notation)
function About() 

{
var user={'name':'Milan Thomas','age':23,'place':'Ernakulam','phone':7654578965,'email':'milan@gmail.com','gender':'female'}//Object

  

  return (
    <div><div class="container fst-italic bg-light p-5 w-75 mt-3">
      <h3 class="text-center">About Me</h3>
      <div class="row">
        <div class="col-6 mt-2">Name:<b>{user.name}</b></div>
        <div class="col-6 mt-2">Age:<b>{user.age}</b></div>
        <div class="col-6 mt-2">Place:<b>{user.place}</b></div>
        <div class="col-6 mt-2">Phone:<b>{user.phone}</b></div>
        <div class="col-6 mt-2">email:<b>{user.email}</b></div>
        <div class="col-6 mt-2">gender:<b>{user.gender}</b></div>
      </div>
      
      </div></div>
  )
}

export default About