import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { deleterecipedetail, getrecipedetail, reviews } from '../services/Apicall'

function Detail() {
    const [recipe,setrecipe]=useState({})
    const [review,setreview]=useState([])
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
function editrecipe(i){
    console.log(i)
    navigate(`/edit?id=${i}`)
}
async function deleterecipe(i){
    let res=await deleterecipedetail(i)
    console.log(res)
}
async function allreviews(i){
    let res=await reviews(i)
    setreview(res.data)
    console.log(res.data)
}
function createreview(id){
    navigate(`/addreview?id=${id}`)
}



useEffect(()=>{recipedetail()},[])

  return (
    <div>
      <div class="container p-5 w-50 mt-5 border border-2 shadow">


<div class="container w-50 pb-5 pt-3">
    <h3 class="text-center">{recipe.recipe_name}</h3>
    <div class="d-flex justify-content-center">
    
    <img src={recipe.image} height="300px" width="400px"></img>
    </div>
</div>
<table class="table table-bordered">
    <tbody>
    <tr style={{textAlign:"justify"}}>
        <th>Instructions</th>
        <td>{recipe.instructions}</td>
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
        <td>{recipe.mealtypes}</td>
    </tr>
    </tbody>
</table>
<div class="d-flex justify-content-between mt-5">
    <button class="btn btn-primary" onClick={()=>{editrecipe(recipe.id)}}>Update</button>
    <button class="btn btn-primary" onClick={()=>{deleterecipe(recipe.id)}}>Delete</button>
    <button class="btn btn-primary" onClick={()=>{allreviews(recipe.id)}}>Reviews</button>
    <button class="btn btn-primary" onClick={()=>{createreview(recipe.id)}}>Add new review</button>
</div>
<div>
    <hr></hr>
    <h4>Top Listed Reviews</h4>
    <hr></hr>
    
    {review.map((i)=><div>
        <p>Reviewed By:{i.user}</p>
        <p>Rating:{'*'.repeat(i.rating)}</p>
        <p>Comment:{i.comment}</p>
        <p>Reviewed on:{i.created_at}</p>
        
        </div>
        )}
</div>

    </div>
    </div>
  )
}

export default Detail
