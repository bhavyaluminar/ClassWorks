import React from 'react'
import {Link} from 'react-router-dom'
import { logout } from '../services/Apicall'
function Navbar() {
  async function userlogout(){
      let res=await logout()
      console.log(res) 
  
      localStorage.clear() //deletes the token stored in local Storage
      console.log(localStorage.getItem('Token'))
      //fun()//3.calls checkloginstatus() when user is logged out
      navigate('/login')
     
    }
  return (
    <div>
      
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand fs-3 fst-italic" href="#">Recipe Management System</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mx-auto mb-2 mb-lg-0">

        <li class="nav-item">
            <Link to="/">
          <a class="nav-link" aria-current="page" >Home</a></Link>
        </li>
         <li class="nav-item">
           <Link to="/register">
          <a class="nav-link" aria-current="page" href="#">Register</a></Link>
        </li>
         <li class="nav-item">
          <Link to="/login">
          <a class="nav-link" aria-current="page" href="#">Login</a></Link>
        </li>
         <li class="nav-item">
         <a class="nav-link" onClick={userlogout}>Logout</a>
        </li>
     
     
      </ul>
      <div class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </div>
    </div>
  </div>
</nav>

    </div>
  )
}

export default Navbar
