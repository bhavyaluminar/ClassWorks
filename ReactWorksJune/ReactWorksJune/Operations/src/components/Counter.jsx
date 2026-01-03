import React, { useState } from 'react'

function Counter() {
   const [count,setcount]=useState(0)
    function increment(){
  
    }
    function decrement(){
  
    }
    function reset(){
  
    }
  return (
    <div>
    <div class="container text-center p-5 mt-3 w-25 fst-italic border border-3 shadow">

      <h3 class="mt-3 mb-3">Counter App</h3>
      <div class="mb-3 mt-4">
        <input type="number" value={count} class="form-control border-dark"></input>
      </div>

      <div class="mb-3 mt-5 d-flex justify-content-between">
        <button class="btn btn-outline-dark" onClick={increment}>+</button>
        <button class="btn btn-outline-dark" onClick={decrement}>-</button>
        <button class="btn btn-outline-dark" onClick={reset}>Reset</button>
      </div>


    </div>


    </div>
  )
}

export default Counter