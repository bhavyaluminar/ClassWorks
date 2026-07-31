import axios from 'axios'


//APICALL

//HTTPREQUEST METHODS -get/post/put/patch/delete


// axios.requestmethodname(urladdress,Data,params,headers)


export async function getallbooks(){
    let t=localStorage.getItem("Token")
    let h={'Authorization':"token "+t}
    return await axios.get("http://127.0.0.1:8000/books/",{headers:h})
}


//promise object

//initial state
//resolved -data
//rejected -error


export async function createbook(data){
    let t=localStorage.getItem("Token")
    
    
    let h={'Content-type':'multipart/form-data','Authorization':"token "+t}
    return await axios.post('http://127.0.0.1:8000/books/',data,{headers:h})

}

export async function deletebook(id){
    let t=localStorage.getItem("Token")
    let h={'Authorization':"token "+t}
    
    return await axios.delete(`http://127.0.0.1:8000/books/${id}/`,{headers:h})
}


export async function bookdetail(id){
    let t=localStorage.getItem("Token")
    let h={'Authorization':"token "+t}
    return await axios.get(`http://127.0.0.1:8000/books/${id}/`,{headers:h})
}


export async function editbookdetail(id,data){
     let t=localStorage.getItem("Token")
     let h={'Content-type':'multipart/form-data','Authorization':"token "+t}
    return await axios.put(`http://127.0.0.1:8000/books/${id}/`,data,{headers:h})
}
export async function usersignup(data){
    
    
    return await axios.post('http://127.0.0.1:8000/users/',data)

}
export async function userlogin(data){
    
    
    return await axios.post('http://127.0.0.1:8000/login/',data)

}

export async function userlogout(){

    let t=localStorage.getItem('Token')
    let h={'Authorization':"token "+t}
    return axios.get('http://127.0.0.1:8000/logout',{headers:h})
}

export async function searchbookdetails(word){
  //let p={key:value}

  let p={'search':word}

    return await axios.get("http://127.0.0.1:8000/search",{params:p})
}