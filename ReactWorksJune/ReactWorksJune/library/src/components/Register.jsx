import React, { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { usersignup } from '../services/apicalls'
function Register() {
  const [data,setdata]=useState({'username':'','password':'','email':'','first_name':'','last_name':''})
 const navigate=useNavigate()
  async function register(event){
    event.preventDefault()
    console.log(data)
    let res=await usersignup(data)
    console.log(res.data)
    navigate('/login')


  }
  return (
    <div>
      <div class="container w-50   p-5  mt-3">
        <h4 class="text-center">Register</h4>


<form onSubmit={register}>
  <div class="mb-3">
    <input type="text" class="form-control" onChange={(event)=>{setdata({...data,'username':event.target.value})}} placeholder='Username'></input>
  </div>
  <div class="mb-3">
    <input type="password" class="form-control"  onChange={(event)=>{setdata({...data,'password':event.target.value})}}  placeholder='Password'></input>
  </div>
  <div class="mb-3">
    <input type="email" class="form-control"  onChange={(event)=>{setdata({...data,'email':event.target.value})}} placeholder='Email'></input>
  </div>
  <div class="mb-3">
    <input type="text" class="form-control"  onChange={(event)=>{setdata({...data,'first_name':event.target.value})}}  placeholder='First Name'></input>
  </div>
  <div class="mb-3">
    <input type="text" class="form-control"  onChange={(event)=>{setdata({...data,'last_name':event.target.value})}}  placeholder='Last Name'></input>
  </div>
  <div class="mb-3">
    <input type="submit" class="form-control"></input>
  </div>
</form>






                     </div>
    </div>
  )
}

export default Register
