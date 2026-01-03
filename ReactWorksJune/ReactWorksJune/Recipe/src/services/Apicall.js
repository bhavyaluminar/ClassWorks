import axios from 'axios'


export async function getallrecipes(){

   return  await axios.get('http://127.0.0.1:8000/recipes/')
}
export async function postrecipe(data){
    let h={'Content-Type':'multipart/form-data'}

   return  await axios.post('http://127.0.0.1:8000/recipes/',data,{headers:h})
}


export async function getrecipedetail(id){

   return await axios.get(`http://127.0.0.1:8000/recipes/${id}/`)


}
export async function editrecipedetail(id,data){
   console.log(id,data)
   let h={'Content-Type':'multipart/form-data'}
   return await axios.put(`http://127.0.0.1:8000/recipes/${id}/`,data,{headers:h})


}
export async function deleterecipedetail(id){
   
   
   return await axios.delete(`http://127.0.0.1:8000/recipes/${id}/`)


}
export async function register(data)
{   
    
    return await axios.post('http://127.0.0.1:8000/users/',data)
}
export async function login(data)
{   
    
    return await axios.post('http://127.0.0.1:8000/login/',data)
}

export async function logout()
{    
     let t=localStorage.getItem('Token')
     let h={'Authorization':t}
    
    return await axios.get('http://127.0.0.1:8000/logout',{'headers':h})
}
export async function reviews(id)
{    
     
    
    return await axios.get(`http://127.0.0.1:8000/allreviews/${id}`)
}
export async function addreview(data)
{    
     
    let t=localStorage.getItem('Token')
     let h={'Authorization':t}
    return await axios.post('http://127.0.0.1:8000/review/',data,{'headers':h})
}
