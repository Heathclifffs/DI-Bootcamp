console.log("-------------------------------------Part I--------------------------------------------------");

		
		function hello(){
			alert("Hello World");
		}
		setTimeout(hello,2000);	
console.log("-------------------------------------Part II--------------------------------------------------");
				
		var tab;		
		function addp(){
			newp=document.createElement("p");
			newText= document.createTextNode("Hello World");
			newp.appendChild(newText);
			document.getElementById("container").appendChild(newp);
			tab=document.getElementsByTagName("p")
			console.log(tab);
			if(tab.length===5){
				clears()
			}			
			
		}
		setTimeout(addp,2000);	
console.log("-------------------------------------Part III--------------------------------------------------");
		var itter=setInterval(addp,2000);
		document.getElementById("clear").setAttribute("onclick","clears()")
		function clears(){
			clearInterval(itter);
		}
		
