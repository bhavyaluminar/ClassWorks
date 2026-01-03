import axios from 'axios';

//Apicall

//axios.methodname(urladdress,data,params,headers)

export async function getallbooks(){

    console.log('hello')
    let t=localStorage.getItem('Token')
    let h={'Authorization':t}
     return  await axios.get('http://127.0.0.1:8000/books/',{headers:h})
}

//initial state
//resolved  --response data
//rejected -- response error

export async function addbook(data)
{   console.log('hello')
    let t=localStorage.getItem('Token')
    let h={'Content-type':"multipart/form-data",'Authorization':t}
    return await axios.post('http://127.0.0.1:8000/books/',data,{headers:h})
}


export async function deletebooks(id){
    let t=localStorage.getItem('Token')
    let h={'Authorization':t}

    return await axios.delete(`http://127.0.0.1:8000/books/${id}/`,{headers:h}) 
}

export async function getbookdetail(id){
     let t=localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get(`http://127.0.0.1:8000/books/${id}/`,{headers:h}) 
}

export async function editbookdetail(id,data)
{   console.log('hello')
     let t=localStorage.getItem('Token')
   
    let h={'Content-type':"multipart/form-data",'Authorization':t}
    return await axios.put(`http://127.0.0.1:8000/books/${id}/`,data,{headers:h})
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
    
    return await axios.get('http://127.0.0.1:8000/logout',{headers:h})
}

export async function searchbookdetails(word){
    let p={'search':word}
    return await axios.get('http://127.0.0.1:8000/search',{params:p})
}