import React, { useEffect, useState } from 'react'
import { getallbooks } from '../services/Apicalls'
import { deletebooks } from '../services/Apicalls'
import { useNavigate} from 'react-router-dom'
function View() {
  const navigate=useNavigate()
  const [books, setbooks] = useState([])
  async function fetchbooks() {
    let res = await getallbooks()
    console.log(res.data)
    setbooks(res.data)
  }
function detailbook(id){
  console.log(id)
  navigate(`/detail?id=${id}`)
}

function editbook(id){
  console.log(id)
  navigate(`/edit?id=${id}`)
}
  async function deletebook(i){
    console.log(i)
    let res=await deletebooks(i)
    console.log(res)
  }

  useEffect(() => { fetchbooks() }, []) //calls fetchbooks() when the viewcomponent mounts

  return (
    <div>
      <div class="container text-center p-5 mt-5 w-75 fst-italic border border-3 shadow">

        <h3 class="mt-3 mb-3">Book List</h3>
        <table class="table table-bordered">
          <thead>
            <tr>  
              <th>Title</th> <th>Author </th><th>Pages</th><th>Price </th><th>Language </th><th>Image </th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {books.map(
              (i) => <tr>
                <td class="pt-5">{i.title}</td>
                <td class="pt-5">{i.author}</td>
                <td class="pt-5">{i.pages}</td>
                <td class="pt-5">{i.price}</td>
                <td class="pt-5">{i.language}</td>
                <td class="p-3"><img src={i.image} height="100px" width="100px"></img></td>
                <td class="pt-5"><button class="btn btn-outline-secondary" onClick={()=>detailbook(i.id)}>Detail</button>
                    <button class="btn btn-outline-secondary" onClick={()=>editbook(i.id)}>Edit</button>
                    <button class="btn btn-outline-secondary" onClick={()=>deletebook(i.id)}>Delete</button></td>
              </tr>
            )
            }
          </tbody>




        </table>

      </div>
    </div>
  )
}

export default View
