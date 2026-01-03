import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './components/Home.jsx'
import Welcome from './components/Welcome.jsx'
import Hello from './components/Hello.jsx'
function App() {
  const [count, setCount] = useState(0)
  function click(){
    console.log("clicked")
  }

  return (
    <>
      <div>
<Hello name="Arun" age="23" fun={click}/>
      
{/*   
        <Home/>
        <Welcome/> */}

        </div>
    </>
  )
}

export default App
