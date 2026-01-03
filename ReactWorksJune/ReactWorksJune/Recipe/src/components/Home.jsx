import React, { useEffect, useState } from 'react'
import { getallrecipes } from '../services/Apicall'
import { useNavigate } from 'react-router-dom'

function Home() {

const [recipes,setrecipe]=useState([])
const navigate=useNavigate()
async function fetchrecipes(){
let res=await getallrecipes()


let r=res.data
console.log(r)
setrecipe(r)
}
function add(){
    navigate('/add')

}
function detail(i){
    navigate(`/detail?id=${i}`)
}


useEffect(()=>{fetchrecipes()},[])
  return (
    <div>
      <div class="container p-5 mt-5 border border-2 shadow">

<h3 class="text-center">Available Recipes</h3>

   <div class="row">
{recipes.map((i) => <div class="col-4">
    <div class="card mt-3 mx-auto" style={{width:"18rem"}}>
  <img src={i.image} class="card-img-top" height="200px" width="200px" alt="..."></img>
  <div class="card-body text-center">
    <h5 class="card-title">{i.recipe_name}</h5>
     <button onClick={()=>detail(i.id)} class="btn btn-primary">Details</button>
  </div>
</div>
   
</div>


)}

      
   </div>
<div class="d-flex justify-content-center mt-5">
    <button class="btn btn-primary text-center" onClick={add}>Add new Recipe</button>
    </div>

      </div>

     
    </div>
  )
}

export default Home
