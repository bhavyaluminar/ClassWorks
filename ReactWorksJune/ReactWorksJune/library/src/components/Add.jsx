import React, { useState } from 'react'
import { addbook } from '../services/Apicalls'
import {useNavigate} from 'react-router-dom';

function Add() {
  const navigate=useNavigate()
  const [book, setbook] = useState({ 'title': '', 'author': '', 'pages': '', 'price': '', 'language': '', 'image': '' })

  async function postbook(event) {
    event.preventDefault()
    let res=await addbook(book)
    console.log(res)
   if(res.status ==201)
      navigate('/view')
    else{
      alert("can't add data")
    }


  }
  return (
    <div>
      <div class="container text-center p-5 mt-3 w-50 fst-italic border border-3 shadow">

        <h3 class="mt-3 mb-3">Add Book Details</h3>
        <form onSubmit={postbook}>
          <div class="mb-3">
            <input type="text" class="form-control" onChange={(event)=>{setbook({...book,'title':event.target.value})}} placeholder="TITLE"></input>
          </div>
          <div class="mb-3">
            <input type="text" class="form-control" onChange={(event)=>{setbook({...book,'author':event.target.value})}} placeholder="AUTHOR"></input>
          </div>

          <div class="mb-3">
            <input type="number" class="form-control" onChange={(event)=>{setbook({...book,'pages':event.target.value})}} placeholder="PAGES"></input>
          </div>
          <div class="mb-3">
            <input type="number" class="form-control" onChange={(event)=>{setbook({...book,'price':event.target.value})}} placeholder="PRICE"></input>
          </div>
          <div class="mb-3">
            <input type="text" class="form-control" onChange={(event)=>{setbook({...book,'language':event.target.value})}} placeholder="LANGUAGE"></input>
          </div>
          <div class="mb-3">
            <input type="file" class="form-control" onChange={(event)=>{setbook({...book,'image':event.target.files[0]})}}></input>
          </div>
            <div class="mb-3">
            <input type="submit" class="form-control" ></input>
          </div>



        </form>


      </div>
    </div>
  )
}

export default Add
