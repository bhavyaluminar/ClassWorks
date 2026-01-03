import React from 'react'

function Skills() {
  var skills=['frontend','database','backend']
  return (
    <div>
      <div class="container fst-italic bg-light p-5 w-75 mt-3">
      <h3 class="text-center">Skills</h3>
      <ul>


       {skills.map((i)=><li>{i}</li>)}
      
      
      </ul>
      
      </div>
    </div>
  )
}

export default Skills