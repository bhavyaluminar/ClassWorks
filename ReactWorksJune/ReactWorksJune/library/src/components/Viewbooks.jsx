import React, { useState } from 'react'
import { useEffect } from 'react'
import { deletebook, getallbooks } from '../services/apicalls'
import { useNavigate } from 'react-router-dom'

function Viewbooks() {
  const navigate=useNavigate()
const [books,setbooks]=useState([])


async function fetchbooks(){
    let r=await getallbooks()
    console.log(r)
    let d=r.data
    setbooks(d)
}



function detailbook(i){
  navigate(`/detail?id=${i}`)

}
function editbook(i){
  navigate(`/update?id=${i}`)
}



async function bookdelete(i){
 let res=await deletebook(i)
 console.log(res)

 if(res.status=="204"){
  fetchbooks()
 }
 else{
  alert("can't delete book")
 }
}

useEffect(()=>{fetchbooks()},[])//calls  fetchbooks() when the component mounts

  return (
    <div>
      <div class="container w-75  p-5  mt-3">
        <h4 class="text-center">View Books</h4>

 <table class="table table-bordered">
  <thead>
          <tr>
            <th>Image</th>
            <th>Title</th>
            <th>Author</th>
            <th>Pages</th>
            <th>Price</th>
            <th>Language</th>
            <th>Actions</th>
          </tr></thead>
          <tbody>
          {books.map((i)=><tr>
            <td>{i.image_url}</td>
            <td>{i.title}</td>
            <td>{i.author}</td>
            <td>{i.pages}</td>
            <td>{i.price}</td>
            <td>{i.language}</td>
            <td>
              <button class="btn btn-outline-dark" onClick={()=>detailbook(i.id)}>Detail</button>
            <button class="btn btn-outline-dark" onClick={()=>editbook(i.id)}>Edit</button>
            <button class="btn btn-outline-dark" onClick={()=>bookdelete(i.id)}>Delete</button></td>
            
          </tr>)}</tbody>
        </table>

        
       

                     </div>
    </div>
  )
}

export default Viewbooks
