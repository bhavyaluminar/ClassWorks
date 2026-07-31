import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Home from './components/Home'
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Navbar from './components/Navbar'
import Add from './components/Add'
import Detail from './components/Detail'
import Edit from './components/Edit'
import Register from './components/Register'
import Login from './components/Login'
import Addrev from './components/Addrev'
function App() {
  const [count, setCount] = useState(0)
  const [islogin,setlogin]=useState(false)

  function checkloginstatus(){//checks whether the user loggedin or not
    let t=localStorage.getItem('Token')
    console.log('in appcomponent',t)
    setlogin(!(!(t)))       //if token present islogin set to True
                            //else islogin set to false
                      }



  useEffect(()=>{checkloginstatus()},[]) //calls checkloginstatus() when application loads

  return (
    <>
    
     <BrowserRouter>
    <Navbar  fun={checkloginstatus} islogin={islogin}/>
     <Routes>

<Route path="/" element={<Home/>}></Route>
<Route path="/add" element={<Add/>}></Route>
<Route path="/detail" element={<Detail/>}></Route>
<Route path="/edit" element={<Edit/>}></Route>
<Route path="/register" element={<Register/>}></Route>
   <Route path="/login" element={<Login  fun={checkloginstatus}/>}></Route>
    <Route path="/addrev" element={<Addrev/>}></Route>
     </Routes>
     </BrowserRouter>

    
    </>
  )
}

export default App
