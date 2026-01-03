import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { getbookdetail } from '../services/Apicalls'

function Detail() 
{
   const [book,setbook]=useState({})
    const {search}=useLocation()//used to provide the details of url address.here search represents queryparametrs in the address
    console.log(search) //?id=3

    const queryParams=new URLSearchParams(search)//changed into object format {id:3}
    const i=queryParams.get('id') //reads the value from the key id 
    console.log(i)  //displays 3

     async function bookdetail(){

         let res=await getbookdetail(i)
         console.log(res)
         setbook(res.data)

     }



useEffect(()=>{bookdetail()},[])

  return (
    <div>
        <div class="container text-center p-5 mt-5 w-75 fst-italic border border-3 shadow">

        <h3 class="mt-3 mb-3">Book Details</h3>
        <table class="table table-bordered">
          <tbody>
          <tr>
            <th>TITLE</th>
            <td>{book.title}</td>
          </tr>
          <tr>
            <th>AUTHOR</th>
            <td>{book.author}</td>
          </tr>
          <tr>
            <th>PAGES</th>
            <td>{book.pages}</td>
          </tr>
          <tr>
            <th>PRICE</th>
            <td>{book.price}</td>
          </tr>
          <tr>
            <th>LANGUAGE</th>
            <td>{book.language}</td>
          </tr>
          <tr>
            <th>IMAGE</th>
            <td><img src={book.image} class="img-thumbnail" height="200px" width="200px"></img></td>
          </tr>
          </tbody>


        </table>
      </div>
    </div>
  )
}

export default Detail
