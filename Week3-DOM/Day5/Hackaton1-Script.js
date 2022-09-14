//--------------------creaion of differents Games/App blocs 
		console.log("-------------------------------------blocks--------------------------------------------------");
		var gameApp=[{gameName:"HowMany",gameIco:"Howmany.jpg",gameDesc:"Will you able to find how many objects are display on screen ?",button:"click here to play"},{gameName:"BottleOnTheWall",gameIco:"BottleOnTheWall.jpg",gameDesc:"Do you like substractions ? show us how much try yourself",button:"click here to play"},{gameName:"Multiplication",gameIco:"Multiplication.jpg",gameDesc:"Do you know by heart your multiplication table ? try yourself",button:"click here to play"},{gameName:"Calculator",gameIco:"Calculator.jpg",gameDesc:"Do you have trouble with the calculation ? use our calculator",button:"click here to use it"}]
		console.log(gameApp)
		for (const elements of gameApp) {
//--------------------of ico and game name 
			newdiv0=document.createElement('div');
			newdiv0.setAttribute("id",elements.gameName)
			newdiv0.setAttribute("class","app")
			newdiv1=document.createElement('div');
			newimg=document.createElement('img');
			newimg.setAttribute("src",elements.gameName+"/"+elements.gameIco)
			newimg.setAttribute("width","100px")
			newimg.setAttribute("height","100px")
			newimg.style.border="solid black 3px"
			newimg.style.borderRadius="50px"
			newimg.setAttribute("alt",elements.gameName+" ico")
			newp1=document.createElement('p');
			newp1.style.fontWeight="bold"
			newText1=document.createTextNode(elements.gameName);
			newp1.appendChild(newText1);
			newdiv1.appendChild(newimg);
			newdiv1.appendChild(newp1);
			newdiv0.appendChild(newdiv1);
//-------------------- game desc
			newdiv2=document.createElement('div');
			newp2=document.createElement('p');
			newText2=document.createTextNode(elements.gameDesc);
			newp2.appendChild(newText2);
			newdiv2.appendChild(newp2);
			newdiv0.appendChild(newdiv2);
//-------------------- game button
			newdiv3=document.createElement('div');
			newbutton3=document.createElement('button');
			newText3=document.createTextNode(elements.button);
			newbutton3.appendChild(newText3);
			newbutton3.setAttribute("onclick","confirmation(event)")
			newbutton3.setAttribute("return","false")
			newbutton3.setAttribute("id",elements.gameName)
			newdiv3.appendChild(newbutton3);
			newdiv0.appendChild(newdiv3);
			document.getElementById("content").appendChild(newdiv0)
		}



function confirmation() {
	result = confirm("Would you like to Launch "+event.target.id+" ?" );
	if (result == true) {
		  console.log( event.target)
		   window.open("./"+event.target.id+"/"+event.target.id+".html",'popup',"width=700, height=630,  resizable=none, scrollbars=no")
	}
}
/*Harold Ezekiel Yipene BASSOLE  or Heathclifffs:wrote it the sat 09 sept 2022 start it at 14h57 finish 19h00  difficulty -easiest one , and don't really know what i'm doing everythings are OK!!!! like this word OK...so  go for next chall XD*/






		  
