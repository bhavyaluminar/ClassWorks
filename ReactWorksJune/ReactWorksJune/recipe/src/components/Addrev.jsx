import React, { useState } from 'react'
import { useLocation } from 'react-router-dom'
import { postreview } from '../services/apicalls'

function Addrev() {
  const [review, setreview] = useState({ 'recipe': '', 'comment': '', 'rating': '' })
  const { search } = useLocation()
  const queryParams = new URLSearchParams(search) //{'id':3}
  const i = queryParams.get('id') //fetch the id value from queryParams
  console.log(i)

  async function createreview(event) {
    event.preventDefault()

    review.recipe = i
    console.log(review)

    let res = await postreview(review)
    console.log(res)



  }


  return (
    <div class="container w-50 mt-5 p-4">
      <form onSubmit={createreview}>
        <div class="mb-3">
          <input type="number" min="1" max="5" class="form-control" onChange={(event) => { setreview({ ...review, 'rating': event.target.value }) }} placeholder='Rating'></input>
        </div>

        <div class="mb-3">
          <textarea class="form-control" placeholder='Write your comment here' onChange={(event) => { setreview({ ...review, 'comment': event.target.value }) }}></textarea>
        </div>
        <div class="mb-3">
          <input type="submit" class="btn btn-primary"></input>
        </div>
      </form>
    </div>

  )
}

export default Addrev
