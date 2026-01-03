import { useState } from 'react'

import './App.css'
import Home from './components/Home'
import Navbar from './components/Navbar'
import Counter from './components/Counter'
import Calculator from './components/Calculator'
import Tempconverter from './components/Tempconverter'
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Calorie from './components/Calorie'

function App() {


  return (
    <>
      <div>
        {/* <Navbar/>
        <Home/>
     
<Counter/> 
<Calculator/>
<Tempconverter/> */}

<BrowserRouter>
<Navbar/>
<Routes>
<Route path='/' element={<Home/>}></Route>
   <Route path='/counter' element={<Counter/>}></Route>
    <Route path='/calculator' element={<Calculator/>}></Route>
     <Route path='/tempconv' element={<Tempconverter/>}></Route>
     <Route path='/calorie' element={<Calorie/>}></Route>
</Routes>


</BrowserRouter>





        </div>
    </>
  )
}

export default App
