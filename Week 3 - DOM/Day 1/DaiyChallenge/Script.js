//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		var planets=["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"];
		console.log(planets);
//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		newdiv=[];
		newp=[];
		newTextNode=[];
		for (var i=0;i<8;i++) {
			newdiv[i]=document.createElement('div')
			newp[i]=document.createElement('p')
			newTextNode[i] = document.createTextNode(planets[i]);
			console.log(newTextNode[i]);
			newp[i].appendChild(newTextNode[i]);
			newdiv[i].appendChild(newp[i]);
			newdiv[i].setAttribute("class","planet");
			console.log(newdiv[i]);
//--------------------3
			console.log("-------------------------------------3--------------------------------------------------");
			newdiv[i].classList.add("planet"+(i+1));
			newdiv[i].style.backgroundColor="rgb(1"+(3*i)+"1,1"+(1*i)+"1,1"+(2*i)+"1)";
			console.log(newdiv[i]);
//--------------------4
			console.log("-------------------------------------4--------------------------------------------------");
			var changer=document.body.lastElementChild.previousElementSibling;
			console.log(changer);
			changer.appendChild(newdiv[i]);
		}
//--------------------bonuses
			console.log("-------------------------------------Bonuses--------------------------------------------------");
			var moons=["Sun","Moon"]
			for (j=0;j<moons.length;j++){
				newdiv[j]=document.createElement('div');
				newp[j]=document.createElement('p')
				newTextNode[j] = document.createTextNode(moons[j]);
				console.log(newTextNode[j]);
				newp[j].appendChild(newTextNode[j]);
				newdiv[j].appendChild(newp[j]);
				newdiv[j].setAttribute("class","moon");
				console.log(newdiv[j]);
				newdiv[j].style.backgroundColor="rgb(1"+(2*i)+"1,1"+(1*i)+"1,1"+(0*i)+"1)";
				console.log(newdiv[j]);
				changer.appendChild(newdiv[j]);
			}
			changer1=document.getElementsByClassName("moon");
			changer2=document.getElementsByClassName("planet");
			console.log(changer1);
			document.body.style.marging="auto"
			for (const elements of changer1) {
				elements.style.display="inline";
				//elements.style.padding="";
			}
			for (const element of changer2) {
			//	element.style.width="80%";
				element.style.display="inline-block";
			}
