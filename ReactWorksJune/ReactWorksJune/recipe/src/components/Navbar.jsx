import React from 'react'
import {Link} from 'react-router-dom';
import { userlogout } from '../services/apicalls';
function Navbar({fun,islogin}) {

  async function logout(){
   console.log('hello')
   let res=await userlogout()
   console.log(res)
   localStorage.clear()
   fun()
   console.log(localStorage.getItem('Token'))
  }
  return (
    <div>
     <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Recipe Management</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mx-auto fs-5 mb-2 mb-lg-0">
        <li class="nav-item">
            <Link to="/">
          <a class="nav-link" aria-current="page" href="#">Home</a></Link>
        </li>
        {islogin && <>
         <li class="nav-item">
            
          <a class="nav-link" onClick={logout}>Logout</a>
        </li>
        </>}
        {!islogin && <>
         <li class="nav-item">
          <Link to="/register">
          <a class="nav-link" href="#">Register</a></Link>
        </li>
         <li class="nav-item">
           <Link to="/login">
          <a class="nav-link" href="#">Login</a></Link>
        </li>
        </>}
        
        
       
      </ul>
      {islogin && <><form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form></>
}
    </div>
  </div>
</nav>
    </div>
  )
}

export default Navbar
