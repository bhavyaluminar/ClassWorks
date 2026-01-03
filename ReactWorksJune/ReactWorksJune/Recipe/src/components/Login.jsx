import React, { useState } from 'react'
import { login } from '../services/Apicall'
import { useNavigate } from 'react-router-dom'

function Login() {
  const navigate=useNavigate()
  const [user,setuser]=useState({'username':'','password':''})
  async function userlogin(event){
    event.preventDefault()
    
    let res=await login(user)
    let t=res.data['token']
    localStorage.setItem('Token','token '+t)  //to store  token number

    console.log(localStorage.getItem('Token')) //to read token number
    // fun()  //2.calls checkloginstatus()  when user is logged in
    navigate('/')
  }



  
  return (
   <div>
        <div class="container text-center p-5 mt-3 w-25 fst-italic border border-3 shadow">

      <h3 class="mt-3 mb-3">Login</h3>
       <form onSubmit={userlogin}>
      <div class="mb-3">
        <input  type="text" class="form-control"  onChange={(event)=>setuser({...user,'username':event.target.value})} placeholder="Username"></input>
      </div>
      <div class="mb-3">
        <input  type="password" class="form-control" onChange={(event)=>setuser({...user,'password':event.target.value})} placeholder="Password"></input>
      </div>
     
      <div class="mb-3">
        <input  type="submit" class="form-control" ></input>
      </div>
    </form>

      
    </div>
    </div>
  )
}

export default Login
