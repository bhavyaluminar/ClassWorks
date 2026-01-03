import React, { useState } from 'react'

function Calorie() {
    const [data,setdata]=useState({'weight':'','height':'','age':'','gender':'','activity':''})
    function calculate(){
      console.log(data)
     let bmr,c;

   //Find bmr 
       //  10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (man)

       // 10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161 for ​(woman)
       if(data.gender=="male"){
        bmr=10 * Number(data.weight) + 6.25 * Number(data.height)- 5 * Number(data.age) + 5
       }
      else{
        bmr=10 * Number(data.weight) + 6.25 * Number(data.height)- 5 * Number(data.age) -161
      }

   //find calorie=bmr*activity
     c=bmr*data.activity 
     console.log(bmr,c)

    }
  return (
    <div>
      <div class="container text-center p-5 mt-3 w-25 fst-italic border border-3 shadow">

      <h3 class="mt-3 mb-3">Calorie Calculator</h3>
      <div class="mb-3 mt-4">
        <input type="number" class="form-control border-dark" onChange={(event)=>{setdata({...data,'weight':event.target.value})}} placeholder='Weight'></input>
      </div>
      <div class="mb-3 mt-4">
        <input type="number" class="form-control border-dark" onChange={(event)=>{setdata({...data,'height':event.target.value})}}  placeholder='Height'></input>
      </div>
       <div class="mb-3 mt-4">
        <input type="number" class="form-control border-dark" onChange={(event)=>{setdata({...data,'age':event.target.value})}} placeholder='Age'></input>
      </div>
       <div class="mb-3 mt-4">
        <select class="form-select  border-dark" onChange={(event)=>{setdata({...data,'gender':event.target.value})}} >
        <option value="">Gender</option>
        <option value="male">Male</option>
         <option value="female">female</option>
        </select>
      </div>
       <div class="mb-3 mt-4">
        <select class="form-select  border-dark" onChange={(event)=>{setdata({...data,'activity':event.target.value})}} >
         <option value="">Activity Levels</option>
         <option value="1.2">Sedentary</option>
         <option value="1.375">LightlyActive</option>
         <option value="1.55">ModeratelyActive</option>
         <option value="1.725">VeryActive</option>
         <option value="1.9">ExtraActive</option>
         </select>
      </div>

      

  <div class="mb-3 mt-4">
        <input type="button" value="Calculate" onClick={calculate} class="form-control border-dark"></input>
      </div>

        <div class="mb-3 mt-4">
        <h3>You neeed {c} calorie inorder to maintain current weight</h3>
      </div>


    </div>




    </div>
  )
}

export default Calorie
