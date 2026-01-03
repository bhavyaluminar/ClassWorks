import React, { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { addreview } from '../services/Apicall'

function Addreview() {
    const navigate=useNavigate()
    const [review,setreview]=useState({'recipe':'','rating':'','comment':''}) 
const {search}=useLocation()//used to provide the details of url address.here search represents queryparametrs in the address
    console.log(search) //?id=3

    const queryParams=new URLSearchParams(search)//changed into object format {id:3}
    const i=queryParams.get('id') //reads the value from the key id 
    console.log(i)

    async function postreview(event){
     event.preventDefault()

     review.recipe=i
     let res=await addreview(review)
     console.log(res)
     navigate('/')
     

    }
  return (
    <div>
        <div class="container w-50 p-5 mt-5 border border-2 shadow">


     <form onSubmit={postreview}>
            <div class="mb-3">
                <input type="number" class="form-control" placeholder="Rating(1-5)" onChange={(event)=>{setreview({...review,rating:event.target.value})}}></input>
            </div>
            <div class="mb-3">
                <textarea type="text" class="form-control" placeholder="Comment"  onChange={(event)=>{setreview({...review,comment:event.target.value})}}></textarea>
            </div>
             <div class="mb-3">
                <input type="submit" class="btn btn-primary" value="Addreview"></input>
            </div>
            </form>
    </div>
      </div>
  )
}

export default Addreview
