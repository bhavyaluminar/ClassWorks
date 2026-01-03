import React from 'react'

function Projects()

{
  var projects=['ecommerce','movie','library','recipe']
  return (
    <div> <div class="container fst-italic bg-light p-5 w-75 mt-3">
      <h3 class="text-center">Projects</h3>
      <ol>
       {projects.map((i)=><li>{i}</li>)}
      </ol>
      
      </div></div>
  )
}

export default Projects