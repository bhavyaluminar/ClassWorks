import React, { useState } from 'react'
import { postrecipe } from '../services/Apicall'
import { useNavigate } from 'react-router-dom'

function Add() {
    const navigate=useNavigate()
   const [recipe,setrecipe]=useState({recipe_name:'',ingredients:'',instructions:'',mealtypes:'',cuisine:'',image:''})
    async function addrecipe(event){
        event.preventDefault()
        let res=await postrecipe(recipe)
        console.log(res.data)
        navigate('/')
    
    }
  return (
    <div>
         <div class="container w-50 p-5 mt-5 border border-2 shadow">

<h3 class="text-center">Enter Recipe Detailss</h3>
        <form onSubmit={addrecipe}>
            <div class="mb-3">
                <input type="text" class="form-control" placeholder="Recipename" onChange={(event)=>{setrecipe({...recipe,recipe_name:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <textarea type="text" class="form-control" placeholder="instructions"  onChange={(event)=>{setrecipe({...recipe,instructions:event.target.value})}}></textarea>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" placeholder="Ingredients"  onChange={(event)=>{setrecipe({...recipe,ingredients:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" placeholder="Mealtype"  onChange={(event)=>{setrecipe({...recipe,mealtypes:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" placeholder="Cuisine"  onChange={(event)=>{setrecipe({...recipe,cuisine:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <input type="file" class="form-control"  onChange={(event)=>{setrecipe({...recipe,image:event.target.files[0]})}}></input>
            </div>
             <div class="mb-3">
                <input type="submit" class="form-control"></input>
            </div>
        </form>
      
    </div></div>
  )
}

export default Add
