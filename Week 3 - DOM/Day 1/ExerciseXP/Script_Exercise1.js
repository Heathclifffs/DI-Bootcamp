//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");

		var divContent=document.getElementById("container").innerHTML;
		console.log(divContent);
//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		var change1=document.body.firstElementChild.nextElementSibling.firstElementChild.nextElementSibling
		change1.textContent="Richard";
		console.log(change1);
		console.log(change1.textContent);
//-------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		var change2=document.getElementsByTagName("ul");
		console.log(change2);
		for (const element of change2) {
			changer=element.firstElementChild;
			console.log(changer);
			changer=element.firstElementChild.textContent="Harold"
			console.log(changer);
		}
//------------------4
		console.log("-------------------------------------4--------------------------------------------------");
		var change3=document.getElementsByTagName("li");
		console.log(change3);
		for (const elements of change3) {
			changer1=elements.textContent
			if(changer1==="Sarah"){
				console.log("removing of "+changer1);
				changer11=elements;
				changer11=changer11.outerHTML="";
				console.log(changer11);
				
			}
		}
	

//-------------------bonuses
		console.log("-------------------------------------bonus 1--------------------------------------------------");
		var selected=document.getElementsByTagName("ul");
		for (const element of selected){
			selection=element.classList.add("student_list");
			console.log(selected);
		}
		console.log("-------------------------------------bonus 2--------------------------------------------------");
		var select=document.body.firstElementChild.nextElementSibling;
		console.log(select);
		console.log(select.classList);
		select.classList.add("university","attendance");
		console.log(select);		
	
