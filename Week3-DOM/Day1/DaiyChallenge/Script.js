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

//--------------------bonuses
			console.log("-------------------------------------Bonuses--------------------------------------------------");
			var moons=[]
			var row=document.getElementsByClassName("planet");
				console.log(row);
				var f=0;
			for (j=0;j<planets.length;j++){
				var nb=prompt("how many moons for "+planets[j]);
				f=f+1;
				for(k=0;k<nb;k++){
					newdiv[k]=document.createElement('div');
					newp[k]=document.createElement('p')
					moon=prompt("name of moons "+k);
					newTextNode[k] = document.createTextNode(moon+"."+f);
					console.log(newTextNode[k]);
					newp[k].appendChild(newTextNode[k]);
					newdiv[k].appendChild(newp[k]);
					newdiv[k].setAttribute("class","moon");
					console.log(newdiv[k]);
					newdiv[k].style.backgroundColor="rgb(1"+(2*i)+"1,1"+(1*i)+"1,1"+(0*i)+"1)";
					console.log(newdiv[k]);
					row[j].appendChild(newdiv[k]);
				}
					
			}	
			
