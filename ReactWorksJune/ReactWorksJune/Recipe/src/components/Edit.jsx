import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { editrecipedetail, getrecipedetail } from '../services/Apicall'

function Edit() {
    const [recipe,setrecipe]=useState({})
    const navigate=useNavigate()
 const {search}=useLocation()//used to provide the details of url address.here search represents queryparametrs in the address
    console.log(search) //?id=3

    const queryParams=new URLSearchParams(search)//changed into object format {id:3}
    const i=queryParams.get('id') //reads the value from the key id 
    console.log(i)


async function recipedetail(){
let res=await getrecipedetail(i)
console.log(res.data)
setrecipe(res.data)

}

async function editrecipe(event){
    console.log(recipe)
    event.preventDefault()
   let recipe1={...recipe}
   if (typeof recipe1.image=="string"){
    delete recipe1.image
   }
   console.log(recipe1)
   let res=await editrecipedetail(i,recipe1)
   console.log(res)
   navigate('/')

}

useEffect(()=>{recipedetail()},[])

  return (
    <div>

                 <div class="container w-50 p-5 mt-5 border border-2 shadow">

<h3 class="text-center">Edit Recipe Detailss</h3>
        <form onSubmit={editrecipe}>
            <div class="mb-3">
                <input type="text" value={recipe.recipe_name} class="form-control" placeholder="Recipename" onChange={(event)=>{setrecipe({...recipe,recipe_name:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <textarea type="text" value={recipe.instructions} class="form-control" placeholder="instructions"  onChange={(event)=>{setrecipe({...recipe,instructions:event.target.value})}}></textarea>
            </div>
            <div class="mb-3">
                <input type="text" value={recipe.ingredients} class="form-control" placeholder="Ingredients"  onChange={(event)=>{setrecipe({...recipe,ingredients:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <input type="text" value={recipe.mealtypes} class="form-control" placeholder="Mealtype"  onChange={(event)=>{setrecipe({...recipe,mealtypes:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <input type="text" value={recipe.cuisine} class="form-control" placeholder="Cuisine"  onChange={(event)=>{setrecipe({...recipe,cuisine:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <img src={recipe.image} height="100px" width="100px"></img>
                <input type="file"class="form-control"  onChange={(event)=>{setrecipe({...recipe,image:event.target.files[0]})}}></input>
            </div>
             <div class="mb-3">
                <input type="submit" class="form-control"></input>
            </div>
        </form>
      
    </div>
      
    </div>
  )
}

export default Edit
