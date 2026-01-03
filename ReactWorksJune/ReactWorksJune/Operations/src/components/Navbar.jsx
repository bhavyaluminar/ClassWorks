
import React from 'react';
import {Link} from 'react-router-dom';
function Navbar() {
  return (
    <div><nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand fs-3 fst-italic" href="#">OPERATIONS</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto fst-ialic fs-3 mb-2 mb-lg-0">
        <li class="nav-item">
          <Link to="/">
          <a class="nav-link" aria-current="page" >Home</a></Link>
        </li>
        <li class="nav-item">
          <Link to="/counter">
          <a class="nav-link">Counter</a></Link>
        </li>
        <li class="nav-item">
           <Link to="/calculator">
          <a class="nav-link">Calculator</a></Link>
        </li>
          <li class="nav-item">
            <Link to="/tempconv">
          <a class="nav-link" >Tempconverter</a></Link>
        </li>
         <li class="nav-item">
             <Link to="/calorie">
          <a class="nav-link" >Calorie</a></Link>
        </li>
      
    
      </ul>
     
    </div>
  </div>
</nav></div>
  )
}

export default Navbar