var add
var ero=0;
var tru=0;
var level
var tab1=["Harold.jpg","fish.png","turtle.png","bird.png","rat.png","mike.png"]
var tab2=["6","7","8","9","10"]
var value;
var loops
var chance;
var audio;
var stage;
var selected1;
var selected2;
function init(){
	level=1;
	stage=1;
	chance=3;
	loops.play()
}
loops=new Audio('Welcome.mp3');
audio=new Audio('Yes yes yes.mp3')
loops.loop="true"
loops.volume="0.5"
console.log(loops)

function start(){
	init()
	document.getElementById("displayImg").innerHTML=""
	alert("RULES :click on the correct figure that show how many items are displayed")
	display()
}
function values(event){
	var norm=document.getElementsByClassName("figure")
	for(const e of norm){
		if(e.children[0].style.color==="red" ||e.children[0].style.color==="green"){
			e.children[0].style.color="black"		
		}
	}
	if (!selected2){
		console.log(selected2)
	}else{
		console.log(event.target.textContent)
		value=event.target.textContent;
		value=parseInt(value);
		console.log(value)
		cmp(value,selected2,event.target)
	}
	
}
function display(){
	document.getElementById("stage").innerHTML="level: <span class=\"blue\">"+level+"</span> Stage :<span <span class=\"blue\">"+stage+"</span>"
	document.getElementById("try").innerHTML=" Try Again left: <span <span class=\"blue\">"+chance+"</span>"
	if(stage<2){
		selected1=Math.floor(Math.random() * tab1.length) ;
		selected2=Math.floor(Math.random() *(5-1)+1) ;
		for(var j=1;j<= selected2;j++){
			newimg=document.createElement('img');
			newimg.setAttribute("src",tab1[selected1])
			newimg.setAttribute("width","100px")
			newimg.setAttribute("height","100px")
			newimg.setAttribute("alt","display ico")
			document.getElementById("displayImg").appendChild(newimg)
		}
	}else if(stage===2){
		/*var norm=document.getElementsByClassName("figure")
		for(const e of norm){
			console.log(e)
			//e.setAttribute("heigth","100px")		
		}*/
		add=stage+ero
		ero=ero+1;
		if(add==2){
			for(var j=0;j<=(tab2.length-1);j++){
				newtext=document.createTextNode(tab2[j])
				newp=document.createElement('p');
				newp.appendChild(newtext)
				newdiv=document.createElement('div');
				newdiv.setAttribute("id",tab2[j])
				newdiv.setAttribute("class","figure")
				newdiv.setAttribute("onclick","values(event)")
				newdiv.appendChild(newp)
				console.log(newdiv)
				document.getElementById("displayFigure").appendChild(newdiv)
			}	
		}
		var norm=document.getElementsByClassName("figure")
		for(const e of norm){
			console.log(norm)
			e.setAttribute("heigth","90px")	
			e.style.fontSize="30px"	
		}
		selected1=Math.floor(Math.random() * tab1.length) ;
		selected2=Math.floor(Math.random() *(8-1)+1) ;
		for(var j=1;j<= selected2;j++){
			newimg=document.createElement('img');
			newimg.setAttribute("src",tab1[selected1])
			newimg.setAttribute("width","60px")
			newimg.setAttribute("height","100px")
			newimg.setAttribute("alt","display ico")
			document.getElementById("displayImg").appendChild(newimg)
		
		}
	}else{
		selected1=Math.floor(Math.random() * tab1.length) ;
		selected2=Math.floor(Math.random() *(10-1)+1) ;
		for(var j=1;j<= selected2;j++){
			newimg=document.createElement('img');
			newimg.setAttribute("src",tab1[selected1])
			newimg.setAttribute("width","50px")
			newimg.setAttribute("height","100px")
			newimg.setAttribute("alt","display ico")
			document.getElementById("displayImg").appendChild(newimg)
		}
			
	}
}

function cmp(var1,var2,e){
	if(var1===var2){
		audio= new Audio('Yes yes yes.mp3')
		audio.play()
		document.getElementById("stage").innerHTML="level: <span class=\"blue\">"+level+"</span> Stage :<span <span class=\"blue\">"+stage+"</span>"
		document.getElementById("try").innerHTML=" Try Again left: <span class=\"blue\">"+chance+"</span>"
		e.style.color="green"
		document.getElementById("displayImg").innerHTML=""
		if(level===3){
			stage=stage+1;
			level=0;
		}
		level=level+1;
		if(stage>=3 && chance>0){
			audio= new Audio('Win.mp3')
			audio.play()
			level=3
			stage=3
			alert("you win !!!")
			document.getElementById("displayImg").innerHTML=""
			newtext2=document.createTextNode("CONGRACULATION you have save the kingdom")
			newtext3=document.createTextNode("Click here to do it again")
			newp2=document.createElement('p');
			newp2.appendChild(newtext2)
			newbutton=document.createElement('button');
			newbutton.appendChild(newtext3)
			newbutton.setAttribute("onclick","start()")
			document.getElementById("displayImg").appendChild(newp2)
			document.getElementById("displayImg").appendChild(newbutton)
		}else{
			display()
		}

	}else{	
		audio= new Audio('No No.mp3')
		audio.play()
		chance=chance-1;
		document.getElementById("stage").innerHTML="level: <span class=\"blue\">"+level+"</span> Stage :<span <span class=\"blue\">"+stage+"</span>"
		document.getElementById("try").innerHTML=" Try Again left: <span <span class=\"blue\">"+chance+"</span>"
		e.style.color="red"
		document.getElementById("displayImg").innerHTML=""
		if(chance<=0 && stage<3){
			audio= new Audio('Lose.mp3')
			audio.play()
			alert (" you fail")
			chance=0;
			
			document.getElementById("displayImg").innerHTML=""
			newp2=document.createElement('p');
			newtext2=document.createTextNode("OHHH!! You have failed protecting kingdom")
			newp2.appendChild(newtext2)
			newtext3=document.createTextNode("Click here to try again")
			newbutton=document.createElement('button');
			newbutton.appendChild(newtext3)
			console.log(newbutton)
			newbutton.setAttribute("onclick","start()")
			document.getElementById("displayImg").appendChild(newp2)
			document.getElementById("displayImg").appendChild(newbutton)
			//init()
			
		}else{
			display()
		}
	
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
/*Harold Ezekiel Yipene BASSOLE  or Heathclifffs:wrote it the sat 09 sept 2022 start it at 19h45 finish 04h05  difficulty -hardiest one , was angry and hungry too LOL ,and don't really know what i'm doing css is not achieve go for next chall XD*/






















