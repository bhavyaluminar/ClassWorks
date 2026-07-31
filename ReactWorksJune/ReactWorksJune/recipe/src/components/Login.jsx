import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { userlogin } from '../services/apicalls'

function Login({fun}) {
   const [data,setdata]=useState({'username':'','password':''})


 const navigate=useNavigate()

 async function login(event){
    event.preventDefault()
    console.log(data)
    let res=await userlogin(data)
  

    let t=res.data['token']

    localStorage.setItem("Token",t)
    fun()

    console.log('token number',localStorage.getItem("Token"))
    navigate('/')


  }
  return (
    <div>
        <div class="container w-50   p-5  mt-3">
        <h4 class="text-center">Login</h4>
      <form onSubmit={login}>
  <div class="mb-3">
    <input type="text" class="form-control" onChange={(event)=>{setdata({...data,'username':event.target.value})}} placeholder='Username'></input>
  </div>
  <div class="mb-3">
    <input type="password" class="form-control"  onChange={(event)=>{setdata({...data,'password':event.target.value})}}  placeholder='Password'></input>
  </div>
  
  <div class="mb-3">
    <input type="submit" class="form-control"></input>
  </div>
</form></div>
    </div>
  )
}

export default Login
