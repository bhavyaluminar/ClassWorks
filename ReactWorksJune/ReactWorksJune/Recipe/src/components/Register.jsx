import React, { useState } from 'react'
import { register } from '../services/Apicall'
import {useNavigate} from 'react-router-dom';
function Register() {
  const [user,setuser]=useState({'username':'','password':'','email':'','first_name':'','last_name':''})
  const navigate=useNavigate()
  async function signup(event){
    event.preventDefault()
    let res=await register(user)
    console.log(res)
    navigate('/')
  }
  
  return (
    <div>
        <div class="container text-center p-5 mt-3 w-25 fst-italic border border-3 shadow">

      <h3 class="mt-3 mb-3">Register</h3>

    <form onSubmit={signup}>
      <div class="mb-3">
        <input  type="text" class="form-control"  onChange={(event)=>setuser({...user,'username':event.target.value})} placeholder="Username"></input>
      </div>
      <div class="mb-3">
        <input  type="password" class="form-control" onChange={(event)=>setuser({...user,'password':event.target.value})} placeholder="Password"></input>
      </div>
      <div class="mb-3">
        <input  type="text" class="form-control" onChange={(event)=>setuser({...user,'email':event.target.value})} placeholder="Email"></input>
      </div>
      <div class="mb-3">
        <input  type="text" class="form-control" onChange={(event)=>setuser({...user,'first_name':event.target.value})} placeholder="FirstName"></input>
      </div>
      <div class="mb-3">
        <input  type="text" class="form-control" onChange={(event)=>setuser({...user,'last_name':event.target.value})} placeholder="LastName"></input>
      </div>
      <div class="mb-3">
        <input  type="submit" class="form-control" ></input>
      </div>
    </form>

      
    </div>
    </div>
  )
}

export default Register
