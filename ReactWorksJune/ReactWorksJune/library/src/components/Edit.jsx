import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { editbookdetail, getbookdetail } from '../services/Apicalls'

function Edit() {
  const [book, setbook] = useState({ 'title': '', 'author': '', 'pages': '', 'price': '', 'language': '', 'image': '' })
   const {search}=useLocation()  //1
  const queryParams=new URLSearchParams(search)//changed into object format {id:3}
    const i=queryParams.get('id') //reads the value from the key id 
    console.log(i)  //displays 3

 const navigate=useNavigate()
  async function editbook(event){  //4
  event.preventDefault()
  console.log(book)

   let ubook={...book} //creates the copy of submitted object
   if(typeof ubook.image == "string")//if we dont want to update image field delete the image field from the book object
   {
    delete ubook.image
   }
  console.log(ubook)

let res=await editbookdetail(i,ubook)//calls editbookdetail() with updated book object
 console.log(res)
 navigate('/view')
  }
 async function bookdetail(){    //3

         let res=await getbookdetail(i)
         console.log(res)
         setbook(res.data)

     }
useEffect(()=>{bookdetail()},[]) //2
  
  
  return (
    <div>
      <div class="container text-center p-5 mt-3 w-50 fst-italic border border-3 shadow">

        <h3 class="mt-3 mb-3">Edit Book Details</h3>
        <form onSubmit={editbook}>
          <div class="mb-3">
            <input type="text" value={book.title} class="form-control" onChange={(event)=>{setbook({...book,'title':event.target.value})}} placeholder="TITLE"></input>
          </div>
          <div class="mb-3">
            <input type="text" value={book.author} class="form-control" onChange={(event)=>{setbook({...book,'author':event.target.value})}} placeholder="AUTHOR"></input>
          </div>

          <div class="mb-3">
            <input type="number" value={book.pages} class="form-control" onChange={(event)=>{setbook({...book,'pages':event.target.value})}} placeholder="PAGES"></input>
          </div>
          <div class="mb-3">
            <input type="number" value={book.price}  class="form-control" onChange={(event)=>{setbook({...book,'price':event.target.value})}} placeholder="PRICE"></input>
          </div>
          <div class="mb-3">
            <input type="text" value={book.language} class="form-control" onChange={(event)=>{setbook({...book,'language':event.target.value})}} placeholder="LANGUAGE"></input>
          </div>
          <div class="mb-3">
            <img src={book.image} height="100px" width="100px"></img>
            <input type="file"   class="form-control" onChange={(event)=>{setbook({...book,'image':event.target.files[0]})}}></input>
          </div>
            <div class="mb-3">
            <input type="submit" class="form-control" ></input>
          </div>



        </form>


      </div>
    </div>
  )
}

export default Edit
