import React, { useEffect, useState } from 'react'
import { bookdetail, editbookdetail } from '../services/apicalls'
import { useLocation, useNavigate } from 'react-router-dom'

function Update() {

const [book,setbook]=useState({})

const navigate=useNavigate()

const {search}=useLocation()         //search means portion starting with ?
  console.log(search)                             //?id=5

  
  const queryParams=new URLSearchParams(search)    //{id:5}

  const i=queryParams.get('id')                     //i<=5 

console.log(i)



async function fetchbook(){
 const res=await bookdetail(i)
 console.log(res.data)
 setbook(res.data)}

 async function updatebook(event){
  event.preventDefault()

  console.log(book)

  let res=await editbookdetail(i,book)
  console.log(res)

  if(res.status=="200"){
    navigate('/viewbooks')
  }
  else{
    alert('cant edit book details')
  }



 }

useEffect(()=>{fetchbook()},[])


  return (
    <div>
      <div class="container w-50   p-5  mt-3">
        <h4 class="text-center">Edit Book Details</h4>
        {book.title}
        <form onSubmit={updatebook}>
  <div class="mb-3">
    <input type="text" value={book.title} onChange={(event)=>{setbook({...book,'title':event.target.value})}} class="form-control"  placeholder='Title'></input>
  </div>
  <div class="mb-3">
    <input type="text" value={book.author} onChange={(event)=>{setbook({...book,'author':event.target.value})}} class="form-control" placeholder='Author' ></input>
  </div>
  <div class="mb-3">
    <input type="number" value={book.price} onChange={(event)=>{setbook({...book,'price':event.target.value})}} class="form-control" placeholder='price' ></input>
  </div>
  <div class="mb-3">
    <input type="number" value={book.pages} onChange={(event)=>{setbook({...book,'pages':event.target.value})}} class="form-control" placeholder='pages' ></input>
  </div>
  <div class="mb-3">
    <input type="text" value={book.language} onChange={(event)=>{setbook({...book,'language':event.target.value})}} class="form-control" placeholder='language'></input>
  </div>
  <div class="mb-3">
    <img src={book.image} height="100px" weight="100px"></img>
    <input type="file" class="form-control" onChange={(event)=>{setbook({...book,'image':event.target.files[0]})}}></input>
  </div>
  <div class="mb-3">
    <input type="submit" class="form-control" value="Edit"></input>
  </div>
</form>
                     </div>
    </div>
  )
}

export default Update
