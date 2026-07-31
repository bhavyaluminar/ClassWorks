import React, { useState } from 'react'
import { postrecipe } from '../services/apicalls'
import { useNavigate } from 'react-router-dom'

function Add() {

    const [recipe,setrecipe]=useState({'recipe_name':'','instructions':'','ingredients':'','mealtype':'','cuisine':'','image':''})
const navigate=useNavigate()

    async function addrecipe(event){
        event.preventDefault()
        console.log(recipe)
        let res=await postrecipe(recipe)
        console.log(res)
      if(res.status == "201"){
        navigate('/')
      }
      else{
        alert('cant add recipe')
      }
    }
  return (
    <div>
    
     <div class="container w-25 mt-5">
        <h4 class="text-center mb-4">Add New Recipe Details</h4>    
      <form onSubmit={addrecipe}>
  <div class="mb-3">
    <input type="text" class="form-control" onChange={(event)=>{setrecipe({...recipe,'recipe_name':event.target.value})}} placeholder='Recipe_name'></input>
  </div>
   <div class="mb-3">
    <input type="text" class="form-control"  onChange={(event)=>{setrecipe({...recipe,'ingredients':event.target.value})}} placeholder='Ingredients'></input>
  </div>
   <div class="mb-3">
    <textarea class="form-control"  placeholder='Instructions' onChange={(event)=>{setrecipe({...recipe,'instructions':event.target.value})}}></textarea>
  </div>
   <div class="mb-3">
    <input type="text" class="form-control"  onChange={(event)=>{setrecipe({...recipe,'cuisine':event.target.value})}} placeholder='Cuisine'></input>
  </div>
   <div class="mb-3">
    <input type="text" class="form-control" onChange={(event)=>{setrecipe({...recipe,'mealtype':event.target.value})}} placeholder='Mealtype'></input>
  </div>
   <div class="mb-3">
    <input type="file" class="form-control" onChange={(event)=>{setrecipe({...recipe,'image':event.target.files[0]})}}></input>
  </div>
   <div class="mb-3">
    <input type="submit" class="btn btn-outline-success" value="Add Recipe"></input>
  </div>
  </form>
    </div>
    </div>
  )
}

export default Add
