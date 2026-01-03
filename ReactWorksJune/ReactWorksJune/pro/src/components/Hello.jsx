import React from 'react'

function Hello({name,age,fun}) {
    
  return (
    <div>

        <h1>My name is {name}</h1>
        <h2>Age is {age}</h2>
        <button onClick={fun}>click</button>
    </div>
  )
}

export default Hello
