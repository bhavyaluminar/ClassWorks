import axios from 'axios';


export async function getallrecipes(){

    return await axios.get("http://127.0.0.1:8000/recipes/")

}

export async function postrecipe(data){
    let h={'Content-type':'multipart/form-data'}
    return await axios.post("http://127.0.0.1:8000/recipes/",data,{headers:h})

}
export async function getrecipedetail(id){

    return await axios.get(`http://127.0.0.1:8000/recipes/${id}`)

}

export async function editrecipedetail(id,data){
     let h={'Content-type':'multipart/form-data'}
    return await axios.put(`http://127.0.0.1:8000/recipes/${id}/`,data,{headers:h})

}
export async function deleterecipedetail(id){
    
    return await axios.delete(`http://127.0.0.1:8000/recipes/${id}/`)

}
export async function usersignup(data){
   
    return await axios.post("http://127.0.0.1:8000/users/",data)

}
export async function userlogin(data){
    
    
    return await axios.post('http://127.0.0.1:8000/login/',data)

}


export async function userlogout(){
    
    let t=localStorage.getItem('Token')
    console.log(t)
    let h={'Authorization':'token '+t}
    return await axios.get('http://127.0.0.1:8000/logout',{headers:h})

}

export async function readreviews(i){
    return await axios.get(`http://127.0.0.1:8000/readreview/${i}`)
}


export async function postreview(data){
    
    let t=localStorage.getItem('Token')
    console.log('tokennumber',t)
    let h={'Authorization':'token '+t}
    return await axios.post('http://127.0.0.1:8000/createreview/',data,{headers:h})

}


