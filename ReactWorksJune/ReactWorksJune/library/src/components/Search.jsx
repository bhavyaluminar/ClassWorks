import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import {searchbookdetails} from '../services/Apicalls'

function Search() {
  const [books, setbooks] = useState([])
   const {search}=useLocation()//used to provide the details of url address.here search represents queryparametrs in the address
    console.log(search) //?id=3

    const queryParams=new URLSearchParams(search)//changed into object format {id:3}
    const word=queryParams.get('w') //reads the value from the key id 
    console.log(word) 
    async function searchbooks(){

      let res=await searchbookdetails(word)
      setbooks(res.data)
}



    useEffect(()=>{searchbooks()},[])

  return (
    <div>
        <div class="container text-center p-5 mt-3 w-50 fst-italic border border-3 shadow">

      <h3 class="mt-3 mb-3">Search</h3>
      {Array.isArray(books)
      ?<table class="table table-bordered">
          <thead>
            <tr>  
              <th>Title</th> <th>Author </th><th>Pages</th><th>Price </th><th>Language </th><th>Image </th>
             
            </tr>
          </thead>

          <tbody>
            {books.map(
              (i) => <tr>
                <td class="pt-5">{i.title}</td>
                <td class="pt-5">{i.author}</td>
                <td class="pt-5">{i.pages}</td>
                <td class="pt-5">{i.price}</td>
                <td class="pt-5">{i.language}</td>
                <td class="p-3"><img src={i.image_url} height="100px" width="100px"></img></td>
                
              </tr>
            )
            }
          </tbody>
</table>:<h2>No Results</h2>}
       
      
    </div>
    </div>
  )
}

export default Search
