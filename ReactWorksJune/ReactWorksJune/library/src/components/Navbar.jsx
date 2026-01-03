import React, { useState } from 'react'
import {Link, useNavigate} from 'react-router-dom'
import { logout } from '../services/Apicalls'
function Navbar({fun,islogin}) {
  const [word,setword]=useState()
  const navigate=useNavigate()
  async function userlogout(){
    let res=await logout()
    console.log(res) 

    localStorage.clear() //deletes the token stored in local Storage
    console.log(localStorage.getItem('Token'))
    fun()//3.calls checkloginstatus() when user is logged out
    navigate('/login')
   
  }
  function search(){
    console.log('helo')
    console.log(word)
    navigate(`/search?w=${word}`)
  }
  

  
  return (
   <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand fst-italic fs-3" href="#">Library</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mx-auto mb-2 fst-italic fs-4  mb-lg-0">
        <li class="nav-item">
            <Link to="/"><a class="nav-link" aria-current="page" href="#">Home</a></Link>
          
        </li>

      {islogin &&
      <>
      <li class="nav-item">
          <Link to='/view'><a class="nav-link" href="#">ViewBooks</a></Link>
        </li>
        <li class="nav-item">
            <Link to='/add'> <a class="nav-link" href="#">AddBooks</a></Link>
         
        </li>
         <li class="nav-item">
          
          <a class="nav-link" onClick={userlogout}>Logout</a>
        </li>
      
      </>
      }
    {!islogin && 
    <>
    <li class="nav-item">
            <Link to='/register'>
          <a class="nav-link" href="#">Register</a></Link>
        </li>
        <li class="nav-item">
            <Link to='/login'> <a class="nav-link" href="#">Login</a></Link>
         
        </li>
    </>
    }
        
      </ul>

      {islogin && 
      <>
       <div class="d-flex">
        <input class="form-control me-2" type="search" onChange={(event)=>{setword(event.target.value)}} placeholder="Search" aria-label="Search"></input>
        <button class="btn btn-outline-success" type="submit" onClick={search}>Search</button>
      </div>
      </>}
     
    </div>
  </div>
</nav>
      
  
    </div>
  )
}

export default Navbar
