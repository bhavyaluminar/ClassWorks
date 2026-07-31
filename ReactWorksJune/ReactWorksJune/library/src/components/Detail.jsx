import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { bookdetail } from '../services/apicalls'



function Detail() {

  const location=useLocation()     //full url address detail
  // console.log(location)
  const [book,setbook]=useState({})

  const {search}=useLocation()         //search means portion starting with ?
  console.log(search)                             //?id=5

  
  const queryParams=new URLSearchParams(search)    //{id:5}

  const i=queryParams.get('id')                     //i<=5 

console.log(i)




async function fetchbook(){
 const res=await bookdetail(i)
 console.log(res)

 setbook(res.data)
}

useEffect(()=>{fetchbook()},[])
  return (
    <div>
       <div class="container w-50  p-5  mt-3">
        <h4 class="text-center">Detail Page</h4>
         <table class="table table-bordered mt-3  text-center">
          <tbody>
          <tr>
            <th>Title</th>
            <td>{book.title}</td>
          </tr>

          <tr>
            <th>Author</th>
            <td>{book.author}</td>
          </tr>

          <tr>
            <th>Price</th>
            <td>{book.price}</td>
          </tr>
          <tr>
            <th>Pages</th>
            <td>{book.pages}</td>
          </tr>
          <tr>
            <th>Language</th>
            <td>{book.language}</td>
          </tr>
          <tr>
            <th>Image</th>
            <td><img src={book.image} height="150px" wdith="200px"></img></td>
          </tr></tbody>
         </table>





                     </div>
      
    </div>
  )
}

export default Detail
