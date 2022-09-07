//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		console.log(document.querySelectorAll('[selected]'));
		var select1=document.querySelectorAll('[selected]')[0].value
		console.log(select1)
		alert(select1)
//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		newoption=document.createElement("option");
		newoption.setAttribute("value","classic");
		newText= document.createTextNode("classic");
		newoption.appendChild(newText);
		console.log(newoption);
		document.getElementById("genres").appendChild(newoption)


//--------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		document.getElementById("genres").children[2].selected=true;
		console.log(document.getElementById("genres").children[2]);
