//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		let shoppingList=[]

//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		newform=document.createElement("form");
		newinput=document.createElement("input");
		newinput.setAttribute("placeholder","your artile")
		newinput.setAttribute("id","val");
		newbutton=document.createElement("button");
		newText= document.createTextNode("AddItem");
		newbutton.setAttribute("onclick","addItem()");
		newbutton.appendChild(newText);
		newbutton.addEventListener("click",function(event){
		event.preventDefault()
		});
		newform.appendChild(newinput);
		newform.appendChild(newbutton);
		document.getElementById("root").appendChild(newform);
//--------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		function addItem(){
			var select=document.getElementById("val").value;
			console.log(select);
			shoppingList[shoppingList.length]=select;

			console.log("votre liste de courses")
			for (const element of shoppingList){
				console.log(element);
				alert(element)
			}

		}	
//--------------------4
		console.log("-------------------------------------4--------------------------------------------------");
		newbutton2=document.createElement("button");
		newText2 = document.createTextNode("clearAll");
		newbutton2.setAttribute("onclick","clearAll()");
		newbutton2.appendChild(newText2);
		newbutton2.addEventListener("click",function(event){
		event.preventDefault()
		});
		document.getElementById("root").appendChild(newbutton2);

//--------------------5
		console.log("-------------------------------------5--------------------------------------------------");
		function clearAll(){
			console.log(shoppingList)
			shoppingList.length=0;
			console.log("votre liste de courses est vide");
			alert("votre liste de courses est vide");
		}





















		
