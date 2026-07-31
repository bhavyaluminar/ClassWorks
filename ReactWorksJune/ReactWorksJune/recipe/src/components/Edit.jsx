import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { editrecipedetail, getrecipedetail } from '../services/apicalls'

function Edit() {
      const [recipe,setrecipe]=useState({'recipe_name':'','instructions':'','ingredients':'','mealtype':'','cuisine':'','image':''})
  
 const {search}=useLocation()
   const queryParams=new URLSearchParams(search) //{'id':3}
const i=queryParams.get('id') //fetch the id value from queryParams
console.log(i)  // displays id 3



  
async function fetchrecipe()
{
    let res=await getrecipedetail(i)
    console.log(res.data)
    setrecipe(res.data)
}

async function editrecipe(){

      let res=await editrecipedetail(i,recipe)
      console.log(res)
}



  useEffect(()=>{fetchrecipe()},[])
      return (
    <div>
        <div class="container mt-1 p-5 w-50">
<form onSubmit={editrecipe}>
  <div class="mb-3">
    <input type="text" class="form-control" value={recipe.recipe_name} onChange={(event)=>{setrecipe({...recipe,'recipe_name':event.target.value})}} placeholder='Recipe_name'></input>
  </div>
   <div class="mb-3">
    <input type="text" class="form-control" value={recipe.ingredients}  onChange={(event)=>{setrecipe({...recipe,'ingredients':event.target.value})}} placeholder='Ingredients'></input>
  </div>
   <div class="mb-3">
    <textarea class="form-control"  value={recipe.instructions}  placeholder='Instructions' onChange={(event)=>{setrecipe({...recipe,'instructions':event.target.value})}}></textarea>
  </div>
   <div class="mb-3">
    <input type="text" class="form-control" value={recipe.cuisine}  onChange={(event)=>{setrecipe({...recipe,'cuisine':event.target.value})}} placeholder='Cuisine'></input>
  </div>
   <div class="mb-3">
    <input type="text" class="form-control" value={recipe.mealtype} onChange={(event)=>{setrecipe({...recipe,'mealtype':event.target.value})}} placeholder='Mealtype'></input>
  </div>
   <div class="mb-3">
    <input type="file" class="form-control" onChange={(event)=>{setrecipe({...recipe,'image':event.target.files[0]})}}></input>
  </div>
   <div class="mb-3">
    <input type="submit" class="btn btn-outline-success" value="Edit Recipe"></input>
  </div>
  </form>
</div>
    </div>
    
  )
}

export default Edit
