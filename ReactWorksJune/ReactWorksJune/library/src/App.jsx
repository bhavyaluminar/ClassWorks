import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Home from './components/Home'
import Addbooks from './components/Addbooks'
import Viewbooks from './components/Viewbooks'
import Detail from './components/Detail'
import Login from './components/Login'
import Update from './components/Update'
import Register from './components/Register'
import Search from './components/Search'
import Navbar from './components/Navbar'
function App() {
  const [islogin,setlogin]=useState(false)

  function checkloginstatus(){//checks whether the user loggedin or not
    let t=localStorage.getItem('Token')
    console.log('in appcomponent',t)
    setlogin(!(!(t)))       //if token present islogin set to True
                            //else islogin set to false
                      }



  const [count, setCount] = useState(0)
  useEffect(()=>{checkloginstatus()},[]) //calls checkloginstatus() when application loads
  return (
    <>
     <BrowserRouter>
     <Navbar  fun={checkloginstatus} islogin={islogin}/>
     <Routes>
     <Route path="" element={<Home/>}></Route>
     <Route path="/addbooks" element={<Addbooks/>}></Route>
     <Route path="/viewbooks" element={<Viewbooks/>}></Route>
     <Route path="/detail" element={<Detail/>}></Route>
     <Route path="/login" element={<Login  fun={checkloginstatus}/>}></Route>
     <Route path="/update" element={<Update/>}></Route>
     <Route path="register" element={<Register/>}></Route>
     <Route path="/search" element={<Search/>}></Route>

     </Routes>
     
     
     </BrowserRouter>
    


    </>
  )
}

export default App
