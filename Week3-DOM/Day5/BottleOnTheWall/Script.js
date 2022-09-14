var error
var score
var limit1
var subnb
var limit2
var move
var tru=0;
var loops
var left
var stage
var audio;
function init(){
	error=0;
	score=0;
	stage=1;
	loops.play()
	left=10;
}
loops=new Audio('Welcome.mp3');
audio=new Audio('Yes yes yes.mp3')
loops.loop="true"
loops.volume="0.5"
console.log(loops)

document.getElementById("validate").addEventListener("click",function(event){
	event.preventDefault()
});
document.getElementById("validate").setAttribute("onclick", "values()")
function start(){
	init()
	document.getElementById("displayImg").innerHTML=""
	document.getElementById("displayImg").style.background=""
	alert("RULE: Input the right answer to and increase your score, you have to do less than 3 errors")
	limit1=Math.floor(Math.random() * (101-10)+10) ;
	move=limit1;
	console.log(limit1)
	newtext=document.createTextNode('Bottles Of Beer Lyrics.We start the song at '+limit1+' bottles')
	newp=document.createElement('p');
	newp.appendChild(newtext)
	newp.style.fontWeight="bold"
	document.getElementById("displayImg").appendChild(newp)
	display()
}
function display(){
	document.getElementById("stage").innerHTML="Stage: <span class=\"blue\">"+stage+"</span>"+" left: <span class=\"blue\">"+left+" </span>"
	document.getElementById("try").innerHTML= " Score: <span class=\"blue\">"+score+"</span>"+" Error:<span class=\"red\">"+error+"</span>"
	limit2=Math.floor(Math.random() * (11-0)+0) ;
	console.log(limit2)
	newtext2=document.createTextNode(move+' bottles on The Wall')
	newp2=document.createElement('p');
	newp2.appendChild(newtext2)
	newtext1=document.createTextNode('Take '+limit2+' down, pass it around \nhow many bottles do we have ?')
	move=move-limit2;
	newp1=document.createElement('p');
	newp1.appendChild(newtext1)
	document.getElementById("displayImg").appendChild(newp2)
	document.getElementById("displayImg").appendChild(newp1)
	

}

function values(event){
	answer=document.getElementById("answer")
	console.log(answer)
	if(!limit1){
		alert("not possible now")	
	}else{
	
		answer=answer.children[0].value	
		answer=parseInt(answer)
		if(!answer && answer!==0){
			alert("invalid input try again")
			audio= new Audio('No No.mp3')
			audio.play()
		}else{
			if(answer===move){
				audio= new Audio('Yes yes yes.mp3')
				audio.play()
				document.getElementById("displayImg").innerHTML=""
				score=score+1;
				stage++
				left=left-1;
				display()
					if(move<=0 || left<=0 ||error>=3){
						if(move<=0 && error<=3){
							audio= new Audio('Win.mp3')
							audio.play()
							alert("------------------------------------winner---------------------------------------------")
							document.getElementById("displayImg").innerHTML=""
							newtext2=document.createTextNode("CONGRACULATION you have save the princess")
							newtext3=document.createTextNode("Click here to do it again")
							newp2=document.createElement('p');
							newp2.appendChild(newtext2)
							newbutton=document.createElement('button');
							newbutton.appendChild(newtext3)
							newbutton.setAttribute("onclick","start()")
							document.getElementById("displayImg").appendChild(newp2)
							document.getElementById("displayImg").appendChild(newbutton)
							document.getElementById("displayImg").style.background="url(\"background1.jpg\")"
							document.getElementById("displayImg").style.backgroundSize="cover"
							
						
						}else if (left<=0 && error<=3){
							audio= new Audio('Win.mp3')
							audio.play()
							alert("------------------------------------winner---------------------------------------------")
							document.getElementById("displayImg").innerHTML=""
							newtext2=document.createTextNode("CONGRACULATION you have save the princess")
							newtext3=document.createTextNode("Click here to do it again")
							newp2=document.createElement('p');
							newp2.appendChild(newtext2)
							newbutton=document.createElement('button');
							newbutton.appendChild(newtext3)
							newbutton.setAttribute("onclick","start()")
							document.getElementById("displayImg").appendChild(newp2)
							document.getElementById("displayImg").appendChild(newbutton)
							document.getElementById("displayImg").style.background="url(\"background1.jpg\")"
							document.getElementById("displayImg").style.backgroundSize="cover"
						}else if(error>=3){
							audio= new Audio('Lose.mp3')
							audio.play()
							alert("------------------------------------you Loose---------------------------------------------")
							error=3;
							document.getElementById("displayImg").innerHTML=""
							newp2=document.createElement('p');
							newtext2=document.createTextNode("OHHH!! You have failed saving the princesse")
							newp2.appendChild(newtext2)
							newtext3=document.createTextNode("Click here to try again")
							newbutton=document.createElement('button');
							newbutton.appendChild(newtext3)
							console.log(newbutton)
							newbutton.setAttribute("onclick","start()")
							document.getElementById("displayImg").appendChild(newp2)
							document.getElementById("displayImg").appendChild(newbutton)
							document.getElementById("displayImg").style.background="url(\"ba.png\")"
							document.getElementById("displayImg").style.backgroundSize="cover"	
							
						}
					}			
			}else{
				//document.getElementById("displayImg").innerHTML=""
				if(error>=3){
					audio= new Audio('Lose.mp3')
					audio.play()
					error=3;
					alert("------------------------------------you Loose---------------------------------------------")	
					document.getElementById("displayImg").innerHTML=""
					newp2=document.createElement('p');
					newtext2=document.createTextNode("OHHH!! You have failed saving the princesse")
					newp2.appendChild(newtext2)
					newtext3=document.createTextNode("Click here to try again")
					newbutton=document.createElement('button');
					newbutton.appendChild(newtext3)
					console.log(newbutton)
					newbutton.setAttribute("onclick","start()")
					document.getElementById("displayImg").appendChild(newp2)
					document.getElementById("displayImg").appendChild(newbutton)
					document.getElementById("displayImg").style.background="url(\"ba.png\")"
					document.getElementById("displayImg").style.backgroundSize="cover"
				}audio= new Audio('No No.mp3')
				audio.play()
				error=error+1;	
				document.getElementById("stage").innerHTML="Stage: <span class=\"blue\">"+stage+"</span>"+" left: <span class=\"blue\">"+left+" </span>"
				document.getElementById("try").innerHTML= " Score: <span class=\"blue\">"+score+"</span>"+" Error:<span class=\"red\">"+error+"</span>"		
			}
		}
		console.log(answer)	
	}
	
}
function songs(event){
	if(tru===0){
		audio.muted="true"
		loops.muted="true"
		tru=1;
	}else if(tru===1){
		audio.muted="false"
		loops.muted="false"
		loops.play()
		console.log(loops)
		tru=0;
	}
		
	
}
var ild=0
function moves(){

	if(ild===0){
		document.getElementById("sidebar").style.top="45px"
		document.getElementById("sidebar").style.bottom="0px"
		ild=ild+1;
		console.log(ild)
	}else{
		document.getElementById("sidebar").style.bottom="65px"
		document.getElementById("sidebar").style.top="0px"
		ild=ild-1;
		console.log(ild)
	}
}
setInterval(moves,1200);


document.onresize=aler()
function aler(){
	alert("\t\t 1-don't resize the page\n\t\t2-Allow Autoplay on your computer to enjoy fully the game")
	console.log(document)
}
/*Harold Ezekiel Yipene BASSOLE  or Heathclifffs :wrote it the sat 10 sept 2022 start it at 8hh59 finish 15h25  difficulty - easy go for next chall XD*/













