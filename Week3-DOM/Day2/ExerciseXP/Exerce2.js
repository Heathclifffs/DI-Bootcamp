//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		console.log(document.body.children[0]);
//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		console.log(document.getElementById("fname"));
		console.log(document.getElementById("lname"));
//--------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		console.log( document.querySelectorAll('[name]'));
//--------------------4
		console.log("-------------------------------------4--------------------------------------------------");
		document.getElementById("submit").addEventListener("click",function(event){
		event.preventDefault()
		});
		var changer=document.body.children[0].children[9];
		changer.setAttribute("onclick","addi()")
		console.log(changer);
		function addi(){
			var change1=document.getElementById("fname").value;
			var change2=document.getElementById("lname").value;
			console.log(change1+" and "+change2);
			if(change1!=="" && change2!==""){
				console.log("valid input");
				newli1=document.createElement("li");
				newTextNode1= document.createTextNode(change1);
				console.log(newTextNode1);
				newli1.appendChild(newTextNode1);
				console.log(newli1);
				newli2=document.createElement("li");
				newTextNode2= document.createTextNode(change2);
				console.log(newTextNode2);
				newli2.appendChild(newTextNode2);
				console.log(newli2);
				change4=changer=document.body.children[1];
				change4.appendChild(newli1);
				change4.appendChild(newli2);
				console.log(change4);
			}else{
				console.log(" one of values is invalid try again");
				alert(" one or both  values are invalid try again");			
			}
			
		
		}
