let secret=Math.floor(Math.random()*20)+1
alert(secret)
let score=20;
let highest=0;
let gameover=false;

function check(){
    if(gameover){
        return; //exits from the function
    }
    //alert('hello')
    let guess=document.getElementById('number').value;
    //alert(guess)

    if(guess==""){

        document.getElementById('msg').innerHTML="No Answer"

    }
    else if(guess==secret){
        document.getElementById('msg').innerHTML="Correct Answer"
        document.body.style.background="green";
        document.getElementById('secret').innerHTML=secret;

        if(score>highest){
            highest=score;
            document.getElementById('highest').innerHTML=highest;
        }
        gameover=true;
    }
    else if(guess>secret){
            document.getElementById('msg').innerHTML="Too High";
            score--;
             document.getElementById('score').innerHTML=score;
    }

    else if(guess<secret){
document.getElementById('msg').innerHTML="Too Low";
            score--;
             document.getElementById('score').innerHTML=score;
    }

}

function again(){
    score=20;
    gameover=false;
    secret=Math.floor(Math.random()*20)+1
    document.getElementById('msg').innerHTML="Start Guessing.....";
     document.body.style.background="#201a1a";
        document.getElementById('secret').innerHTML='?';

      document.getElementById('score').innerHTML=score;
       document.getElementById('guess').innerHTML="";


}
