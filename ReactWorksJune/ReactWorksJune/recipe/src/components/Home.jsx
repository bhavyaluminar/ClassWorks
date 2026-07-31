import React, { useEffect, useState } from 'react'
import { getallrecipes } from '../services/apicalls'
import { useNavigate } from 'react-router-dom'

function Home() {
  const [recipes,setrecipe]=useState([])
  const navigate=useNavigate()

  function detailrecipe(i){
    navigate (`/detail?id=${i}`)
    // console.log('hello')
  }

  function add(){
    navigate('/add')
  }

  async function fetchrecipe(){
    //console.log('hello')
    let res=await getallrecipes()
    console.log(res.data)
    setrecipe(res.data)
  }

  useEffect(()=>{fetchrecipe()},[])
  return (
    <div>
      <div className="container p-5">
        <h4 className="text-center mb-4">Available Recipes</h4>
        <div className="d-flex justify-content-evenly mt-4">
          {recipes.map((i)=><div className="col-4"><div class="card" style={{"width":"22rem"}}>
  <img src={i.image} className="card-img-top" height="300px" alt="..."></img>
  <div className="card-body mx=auto text-center">
    <h5 className="card-title">{i.recipe_name}</h5>
   
    <button onClick={()=>detailrecipe(i.id)} className="btn btn-outline-success">Details</button>
  </div>
</div>

</div>)}

        </div>
    <div className="d-flex justify-content-center mt-4">
      <button className="btn btn-primary" onClick={add}>Add a new Recipe</button>
    </div>   
    </div>
    </div>
  )
}

export default Home