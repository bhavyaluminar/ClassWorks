import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './components/Home'
import Navbar from './components/Navbar'
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Add from './components/Add'
import Detail from './components/Detail'
import Edit from './components/Edit'
import Login from './components/Login'
import Register from './components/Register'
import Addreview from './components/Addreview'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <BrowserRouter>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/add" element={<Add/>}></Route>
           <Route path="/detail" element={<Detail/>}></Route>
             <Route path="/edit" element={<Edit/>}></Route>
             <Route path="/register" element={<Register/>}></Route>
          <Route path="/login" element={<Login/>}></Route>
           <Route path="/addreview" element={<Addreview/>}></Route>
        </Routes>
        </BrowserRouter>
        </div>
    </>
  )
}

export default App
