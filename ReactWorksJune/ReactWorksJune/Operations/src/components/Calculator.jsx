import React, { useState } from 'react'

function Calculator() {
      const [num1,setnum1]=useState('')
      const [num2,setnum2]=useState('')
      const [result,setresult]=useState('')
  
      // function input1(event){
      //   setnum1(event.target.value)
      // }

      //(event)=>{setnum1(event.target.value)}
// function input2(event){
//         setnum2(event.target.value)}

 //(event)=>{setnum2(event.target.value)}
function Add(){
    setresult(Number(num1)+Number(num2))
}
function Sub(){
    setresult(Number(num1)-Number(num2))
}
function Mul(){
    setresult(Number(num1)*Number(num2))
}
function Div(){
    setresult(Number(num1)/Number(num2))
}

  return (
    <div>

<div class="container text-center p-5 mt-3 w-25 fst-italic border border-3 shadow">

      <h3 class="mt-3 mb-3">Arithmetic Calculator</h3>
      <div class="mb-3 mt-4">
        <input type="number" class="form-control border-dark" onChange={(event)=>{setnum1(event.target.value)}}></input>
      </div>
      <div class="mb-3 mt-4">
        <input type="number" class="form-control border-dark" onChange={(event)=>{setnum2(event.target.value)}}></input>
      </div>

      <div class="mb-3 mt-5 d-flex justify-content-between">
        <button class="btn btn-outline-dark" onClick={Add}>+</button>
        <button class="btn btn-outline-dark" onClick={Sub}>-</button>
        <button class="btn btn-outline-dark" onClick={Mul}>*</button>
         <button class="btn btn-outline-dark" onClick={Div}>/</button>
      </div>

  <div class="mb-3 mt-4">
        <input type="number" value={result} class="form-control border-dark"></input>
      </div>

    </div>


    </div>
  )
}

export default Calculator