import React, { useState } from 'react'
import { createbook } from '../services/apicalls'
import {useNavigate} from 'react-router-dom'
function Addbooks() {

  const navigate=useNavigate()

  const [data,setdata]=useState({'title':'','author':'','pages':'','price':'','language':'','image':''})
  
  async function addbook(event){
   event.preventDefault()
   console.log(data)
  let res=await createbook(data)
  
if(res.status=="201"){
  navigate('/viewbooks')
}

else{
 
alert("Cant add new book details")

  }}

  return (
    <div>
    <div class="container w-50   p-5  mt-3">
        <h4 class="text-center">Add Book Details</h4>
<form onSubmit={addbook}>
  <div class="mb-3">
    <input type="text" class="form-control" onChange={(event)=>setdata({...data,'title':event.target.value})} placeholder='Title'></input>
  </div>
  <div class="mb-3">
    <input type="text" class="form-control" placeholder='Author' onChange={(event)=>setdata({...data,'author':event.target.value})}></input>
  </div>
  <div class="mb-3">
    <input type="number" class="form-control" placeholder='price' onChange={(event)=>setdata({...data,'price':event.target.value})}></input>
  </div>
  <div class="mb-3">
    <input type="number" class="form-control" placeholder='pages' onChange={(event)=>setdata({...data,'pages':event.target.value})}></input>
  </div>
  <div class="mb-3">
    <input type="text" class="form-control" placeholder='language' onChange={(event)=>setdata({...data,'language':event.target.value})}></input>
  </div>
  <div class="mb-3">
    <input type="file" class="form-control" onChange={(event)=>setdata({...data,'image':event.target.files[0]})}></input>
  </div>
  <div class="mb-3">
    <input type="submit" class="form-control" value="Add"></input>
  </div>
</form>



</div>
      
    </div>
  )
}

export default Addbooks
