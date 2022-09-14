var timer
var tru=0;
var score;
var totalScore;
var vals=[]
var A=[];
var scoreA;
var loops
var scoreB;
var audio;
var divnumb
var turn
function init(){
	 score=0;
	 timer=30;
	divnumb=4;
	turn=1;
	loops.play()
	scoreA=0;
	scoreB=0;
	totalScore=40;
	
}

loops=new Audio('Welcome.mp3');
audio=new Audio('Yes yes yes.mp3')
loops.loop="true"
loops.volume="0.5"
console.log(loops)

function start(){
	init()
	document.getElementById("displayFigure").style.background=""
	document.getElementById("displayImg").innerHTML=""
	alert("Rule: The Timer will start solve puzzle quickly")
	itter=setInterval(timers,1010);
	display()
}
function display(){
	document.getElementById("stage").innerHTML="Goal: <span class=\"blue\">"+totalScore+"</span>"
	document.getElementById("try").innerHTML= " Score: <span class=\"blue\">"+score+"</span>"+" King Arrival:<span class=\"red\">"+timer+"</span>"
	document.getElementById("displayImg").innerHTML=""
	document.getElementById("displayFigure").innerHTML=""
	for(var i=0;i<=divnumb-1;i++){
		if(i<2){
			newdiv1=document.createElement('div');
			newdiv1.setAttribute("class","figure");
			newdiv1.setAttribute("id","divA"+i);
			A[i]= new Object();
			A[i].x=Math.floor(Math.random() * 11) ;
			A[i].y=Math.floor(Math.random() * 11) ;
			A[i].v=5
			vals[i]=A[i]
			newtext1=document.createTextNode(A[i].x+" swords *"+A[i].y+ " Hammers = ")
			newp1=document.createElement('p');
			newbr=document.createElement('br');
			newp1.appendChild(newtext1)
			newdiv1.appendChild(newp1)
			//newdiv1.setAttribute("width","10%");
			newdiv1.style.width="40%"
			newdiv1.style.marginLeft="1%"
			newdiv1.style.marginTop="2%"
			newdiv1.style.marginBottom="1%"
			newdiv1.style.border="solid black 0.5px"
			newdiv1.style.textAlign="center"
			newdiv1.style.display="inline-block"
			newinput=document.createElement('input');
			newinput.style.width="50%"
			newinput.setAttribute("placeholder","your answer");
			newdiv1.appendChild(newinput)
			newdiv1.appendChild(newbr)
			document.getElementById("displayImg").appendChild(newdiv1)
		}else{
			newdiv1=document.createElement('div');
			newdiv1.setAttribute("class","figure");
			newdiv1.setAttribute("id","divA"+i);
			A[i]= new Object();
			A[i].x=Math.floor(Math.random() * 11) ;
			A[i].y=Math.floor(Math.random() * 11) ;
			A[i].v=5
			vals[i]=A[i]
			newtext1=document.createTextNode(A[i].x+" swords * "+A[i].y+ " Hammers = ")
			newp1=document.createElement('p');
			newbr=document.createElement('br');
			newp1.appendChild(newtext1)
			newdiv1.appendChild(newp1)
			//newdiv1.setAttribute("width","10%");
			newdiv1.style.width="39%"
			newdiv1.style.marginLeft="1%"
			newdiv1.style.marginTop="2%"
			newdiv1.style.marginBottom="1%"
			newdiv1.style.border="solid black 0.5px"
			newdiv1.style.textAlign="center"
			newdiv1.style.display="inline-block"
			newinput=document.createElement('input');
			newinput.style.width="50%"
			newinput.setAttribute("placeholder","your answer");
			newdiv1.appendChild(newinput)
			newdiv1.appendChild(newbr)
			document.getElementById("displayFigure").appendChild(newdiv1)
			
		}
	}
	newbutton=document.createElement('button');
	newtext=document.createTextNode("validate 1")
	newbutton.appendChild(newtext)
	newbutton.addEventListener("click",function(event){
		event.preventDefault()
	});
	newbutton.setAttribute("id","valid1");
	newbutton.setAttribute("onclick","values(event)")
	document.getElementById("displayFigure").appendChild(newbr);
	document.getElementById("displayFigure").appendChild(newbutton);
	
	newbutton1=document.createElement('button');
	newtext1=document.createTextNode("validate 2")
	newbutton1.appendChild(newtext1)
	newbutton1.addEventListener("click",function(event){
		event.preventDefault()
	});
	newbutton1.setAttribute("id","valid2");
	newbutton1.setAttribute("onclick","values(event)")
	newbr1=document.createElement('br');
	document.getElementById("displayImg").appendChild(newbr1)
	document.getElementById("displayImg").appendChild(newbutton1)
	
	
}

function values(event){
	if(timer>0){
		var val1=event.target.parentElement.children[0].children[1].value
		val1=parseInt(val1)
		var val2=event.target.parentElement.children[1].children[1].value
		val2=parseInt(val2)
		var result0=vals[0].x*vals[0].y
		var result1=vals[1].x*vals[1].y
		var result2=vals[2].x*vals[2].y
		var result3=vals[3].x*vals[3].y
		if(val1 === result0 || val1===result2){
			event.target.parentElement.children[0].children[1].style.backgroundColor="lightgreen"
			audio= new Audio('Yes yes yes.mp3')
			audio.play()
		}else{
			event.target.parentElement.children[0].children[1].style.backgroundColor="red"
			audio= new Audio('No No.mp3')
			audio.play()
		}
		if(val2 === result1 || val2===result3){
			event.target.parentElement.children[1].children[1].style.backgroundColor="lightgreen"
			audio= new Audio('Yes yes yes.mp3')
			audio.play()
		}else{
			event.target.parentElement.children[1].children[1].style.backgroundColor="red"
			audio= new Audio('No No.mp3')
			audio.play()
		}
		tab=document.getElementsByTagName("input")
		if(turn===1){
			scoreA=0
			for(const e of tab){
				
				if(e.style.backgroundColor==="lightgreen"){
					scoreA=scoreA+vals[0].v
					console.log(scoreA)
					if(scoreA===20){
						audio= new Audio('Yes yes yes.mp3')
						audio.play()
						timer=timer+20
						turn=2
					}
				}
			}
		}else{	scoreB=0
			for(const e of tab){
				
				if(e.style.backgroundColor==="lightgreen"){
					scoreB=scoreB+vals[0].v
					if(scoreB===20){
						audio= new Audio('Win.mp3')
						audio.play()
						clearInterval(itter);
						alert("\t\t------winner-----")
						document.getElementById("displayImg").innerHTML=""
						document.getElementById("displayFigure").innerHTML=""
						newtext2=document.createTextNode("CONGRACULATION you have save the Village by collecting all weapons")
						newtext3=document.createTextNode("Click here to do it again")
						newp2=document.createElement('p');
						newp2.appendChild(newtext2)
						newbutton=document.createElement('button');
						newbutton.appendChild(newtext3)
						newbutton.setAttribute("onclick","start()")
						document.getElementById("displayImg").appendChild(newp2)
						document.getElementById("displayImg").appendChild(newbutton)
						document.getElementById("displayFigure").style.background="url(\"background1.jpg\")"
						document.getElementById("displayFigure").style.backgroundSize="cover"
					}
				}
			}
		}
		score=scoreB+scoreA;
		console.log(score)
		document.getElementById("stage").innerHTML="Goal: <span class=\"blue\">"+totalScore+"</span>"
		document.getElementById("try").innerHTML= " Score: <span class=\"blue\">"+score+"</span>"+" King Arrival:<span class=\"red\">"+timer+"</span>"
		if(turn===2){
			turn=3
			display()
		}
	}else{
		audio= new Audio('Lose.mp3')
		audio.play()
		alert("----you Lose--------")
		document.getElementById("displayImg").innerHTML=""
		document.getElementById("displayFigure").innerHTML=""
		document.getElementById("displayImg").innerHTML=""
		newp2=document.createElement('p');
		newtext2=document.createTextNode("OHHH!! The king arrived before you finish colleting all weapons and he have destroyed the village")
		newp2.appendChild(newtext2)
		newtext3=document.createTextNode("Click here to try again")
		newbutton=document.createElement('button');
		newbutton.appendChild(newtext3)
		console.log(newbutton)
		newbutton.setAttribute("onclick","start()")
		document.getElementById("displayImg").appendChild(newp2)
		document.getElementById("displayImg").appendChild(newbutton)
		document.getElementById("displayFigure").style.background="url(\"backdes.jpg\")"
		document.getElementById("displayFigure").style.backgroundSize="cover"
	}
}
function timers(){
	timer=timer-1
	document.getElementById("stage").innerHTML="Goal: <span class=\"blue\">"+totalScore+"</span>"
	document.getElementById("try").innerHTML= " Score: <span class=\"blue\">"+score+"</span>"+" King Arrival:<span class=\"red\">"+timer+"</span>"
	if(timer<=0){
		clearInterval(itter);
		values();
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
		document.getElementById("sidebar").style.bottom="100px"
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
/*Harold Ezekiel Yipene BASSOLE or Heathclifffs :wrote it the sat 10 sept 2022 start it at 15h45 finish 22h25  difficulty - very easy go for next chall XD*/
