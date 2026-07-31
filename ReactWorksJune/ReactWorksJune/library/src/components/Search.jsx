import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { searchbookdetails } from '../services/apicalls'

function Search() {

const [books,setbooks]=useState([])
const {search}=useLocation()         //search means portion starting with ?
  console.log(search)                             //?id=5

  
  const queryParams=new URLSearchParams(search)    

  const word=queryParams.get('w')                    

console.log(word)  



async function searchbooks(){
  let res=await searchbookdetails(word)
  console.log(res.data)
  
  setbooks(res.data)
}


  useEffect(()=>{searchbooks()},[])

  return (
    <div>
    <div class="container w-50   p-5  mt-3">
        <h4 class="text-center">Search Results</h4>

{Array.isArray(books)?

        <table class="table table-bordered">
  <thead>
          <tr>
            <th>Image</th>
            <th>Title</th>
            <th>Author</th>
            <th>Pages</th>
            <th>Price</th>
            <th>Language</th>
          
          </tr></thead>
          <tbody>
          {books.map((i)=><tr>
            <td><img src={i.image_url}></img></td>
            <td>{i.title}</td>
            <td>{i.author}</td>
            <td>{i.pages}</td>
            <td>{i.price}</td>
            <td>{i.language}</td>
            
            
          </tr>)}</tbody>
        </table>:<div>No Search Results</div>}
                     </div>
    </div>
  )
}

export default Search
