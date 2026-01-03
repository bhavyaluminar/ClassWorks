import React, { useState } from 'react'

function Tempconverter() {
    const [tempc,settempc]=useState()
    const [tempf,settempf]=useState()

    function input(event){
        settempf('')
     settempc(event.target.value)
    }
    function tempconv(){
        let f=(tempc*1.8)+32
        settempf(f)
    }
  return (
    <div>
      <div class="container text-center p-5 mt-3 w-25 fst-italic border border-3 shadow">
      <h3 class="mt-3 mb-3">Temperature Converter</h3>
      <div class="mb-3 mt-4">
        <input type="number" class="form-control border-dark" onChange={input}></input>
      </div>
     

      <div class="mb-3 mt-5 d-flex justify-content-center">
        <button class="btn btn-outline-dark" onClick={tempconv}>=</button>
        
      </div>

  <div class="mb-3 mt-4">
        <input type="number"  value={tempf} class="form-control border-dark"></input>
      </div>

    </div>
    </div>
  )
}

export default Tempconverter
