
import React from 'react'

function Education() {
  var q=[
    {'course':'Mtech','university':'MG','aggregate':85},
    {'course':'Btech','university':'MG','aggregate':80}
  ]
  return (
    <div> <div class="container fst-italic bg-light p-5 w-75 mt-3">
      <h3 class="text-center">Education</h3>
      <table class="table table-bordered">
        <tbody>
        <tr class="text-center">
          <th>Course</th>
          <th>University</th>
          <th>Aggregate</th>
        </tr>
         {q.map((i)=>
         <tr>
          <td>{i.course}</td>
          <td>{i.university}</td>
          <td>{i.aggregate}</td>
         </tr>
        )}
        </tbody>
      </table>
     
      </div></div>
  )
}

export default Education