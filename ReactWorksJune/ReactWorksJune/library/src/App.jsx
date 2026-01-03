import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Home from './components/Home';
import Add from './components/Add';
import View from './components/View';
import Register from './components/Register';
import Login from './components/Login';
import Navbar from './components/Navbar';
import Detail from './components/Detail';
import Edit from './components/Edit';
import Search from './components/Search';
function App() {
  const [count, setCount] = useState(0)
  const [islogin,setlogin]=useState(false)   //to reorganize navbar,default value is set to false

  function checkloginstatus(){              //to check whether token present or not

    let t=localStorage.getItem('Token')    //if token present islogin set to true else it set to false
    console.log(t)
    setlogin(!(!(t)))
  }


useEffect(()=>{checkloginstatus()},[]) //1 calls checkloginstatus() when application mounts

  return (
    <>
      <div>
        <BrowserRouter>
        <Navbar fun={checkloginstatus} islogin={islogin}/>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/add" element={<Add/>}></Route>
          <Route path="/view" element={<View/>}></Route>
          <Route path="/register" element={<Register/>}></Route>
          <Route path="/login" element={<Login fun={checkloginstatus}/>}></Route>
           <Route path="/detail" element={<Detail/>}></Route>
           <Route path="/edit" element={<Edit/>}></Route>
           <Route path="/search" element={<Search/>}></Route>
        </Routes>
        
        </BrowserRouter>
       </div>
    </>
  )
}

export default App
