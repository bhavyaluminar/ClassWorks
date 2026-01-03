import React from 'react'
import image from '../assets/images/milan.jpg'



function Profile() {
  var name="Milan Thomas" //string type
  
  
  return (
    <div>
   <div class="container-fluid bg-light mt-3">
    <div class="row">
      <div class="col-6 d-flex justify-content-center align-items-center p-2 fst-italic"><h2>Hello,I am {name}</h2></div>
      <div class="col-6 d-flex justify-content-center align-items-center p-2"><img src={image} height="300px" width="300px" class="rounded-circle"></img></div>
    </div>
   </div>


    </div>
  )
}

export default Profile