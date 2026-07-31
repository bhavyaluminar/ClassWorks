import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import {deleterecipedetail, getrecipedetail, readreviews } from '../services/apicalls'

function Detail() {
    const [recipe,setrecipe]=useState({})   //1

   const [review,setreview]=useState()
   const {search}=useLocation()
   const queryParams=new URLSearchParams(search) //{'id':3}
const i=queryParams.get('id') //fetch the id value from queryParams
console.log(i)  // displays id 3
const navigate=useNavigate()
async function detailrecipe(){
    let res=await getrecipedetail(i)
    console.log(res)
    setrecipe(res.data)
}
async function deleterecipe(i){
    let res=await deleterecipedetail(i)
    console.log(res)
    if (res.status=="204"){
        navigate('/')
    }
}

async function readreview(i){
let res=await readreviews(i)
console.log(res)
setreview(res.data)
}

function addreview(i){
    console.log(i)
    navigate(`/addrev?id=${i}`)
}

function editrecipe(i){
    console.log(i)
    navigate(`/edit?id=${i}`)
}
useEffect(()=>{detailrecipe()},[])


  return (
    <div>
      

      <div class="container mt-1 p-5 w-50">
      
        <div class="d-flex justify-content-center">
            <img src={recipe.image} height="300px" width="400px"></img>
        </div>
          <h3 class="text-center mb-5 mt-5">{recipe.recipe_name}</h3>
        <table class="table table-bordered text-center">
            <tbody>
                <tr>
                    <th>Instructions</th>
                    <td style={{"textAlign":"justify"}}>{recipe.instructions}</td>
                </tr>
                 <tr>
                    <th>Ingredients</th>
                    <td>{recipe.ingredients}</td>
                </tr>
                 <tr>
                    <th>Cuisine</th>
                    <td>{recipe.cuisine}</td>
                </tr>
                 <tr>
                    <th>MealType</th>
                    <td>{recipe.mealtype}</td>
                </tr>
            </tbody>
        </table>

        <div class="d-flex justify-content-between mt-5">
            <button class="btn btn-info text-light" onClick={()=>editrecipe(recipe.id)}>Edit</button>
             <button class="btn btn-info text-light" onClick={()=>deleterecipe(recipe.id)}>Delete</button>
              <button class="btn btn-info text-light" onClick={()=>readreview(recipe.id)}>Reviews</button>
               <button class="btn btn-info text-light" onClick={()=>addreview(recipe.id)}>Addreview</button>
        </div>

        <hr></hr>
         {review?
         <>
         <h3>Top Listed Reviews</h3>
        <hr></hr>
        
        
        {review.map((i)=><div>
            <p>Reviewed By:{i.user}</p>
            <p>Rating:<span style={{"color":"gold"}}>{"★".repeat(i.rating)}</span></p>
            <p>Comment:{i.comment}</p>
            <p>Reviewed on:{i.created}</p><hr></hr>
        </div>)}
        
        </>
        :<div></div>}
        







      </div>

      

    </div>
  )
}

export default Detail
