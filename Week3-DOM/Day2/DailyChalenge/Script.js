//--------------------1
		console.log("-------------------------------------1------------------------------------------------------------------------------");
		var select1=document.body.children[1].children[15];
		console.log(select1);
		select1.addEventListener("click",function(event){
		event.preventDefault()
		});
		var changeNoun;
		var changeAdj;
		var changeName;
		var changeVerb;
		var changePlace;
		select1.setAttribute("onclick","calc()")
		function calc(){
			changeNoun=document.getElementById("noun").value;
			console.log("noun="+changeNoun);
    			changeAdj=document.getElementById("adjective").value;
			console.log("adjective= "+changeAdj);
			changeName=document.getElementById("person").value;
			console.log("person= "+changeName);
			changeVerb=document.getElementById("verb").value;
			console.log("verb="+changeVerb);
			changePlace=document.getElementById("place").value;
			console.log("place= "+changePlace);

//--------------------2
		console.log("-------------------------------------2------------------------------------------------------------------------------");
			if(changeNoun!=='' && changeAdj!=='' && changeName!=='' && changeVerb!=='' && changePlace!==''){
				console.log("valid inputs story will be display");
				alert("valid inputs story will be display");
				newp=document.createElement("p");
				newbutton=document.createElement("button");
				newbutton.setAttribute("onclick","news()");
				newTexts= document.createTextNode("click here to change the story");
//--------------------bonuses
		console.log("-------------------------------------bonuses------------------------------------------------------------------------------");
				newbutton.appendChild(newTexts);
				document.body.children[2].appendChild(newbutton);
//--------------------3
		console.log("-------------------------------------3------------------------------------------------------------------------------");
				newText= document.createTextNode("\" "+changeNoun+" is a  man or a woman nobody know.But something is sure "+changeVerb+"ing is his/her passion. The "+changeAdj+" WayS of this activity is the think he/she like.Take him in "+changePlace+" and he/she will impress you more than "+changeName+" \"");
				newp.appendChild(newText);
				console.log(newText);
				console.log(newp);
				document.getElementById("story").appendChild(newText);
			}else{
				console.log("there are invalid inputs try again");
				alert("there are invalid inputs try again");
			}

		}
//--------------------bonuses
		console.log("-------------------------------------bonuses------------------------------------------------------------------------------");
function news(){
	alert("you are here")
	
}
