//------------------2
	console.log("-------------------------------------2--------------------------------------------------");
	var change1=document.body.firstElementChild;
	console.log(change1);
	change1.style.background="lightblue";
	change1.style.padding= "10%";
//------------------3
	console.log("-------------------------------------3--------------------------------------------------");
	var change2=document.getElementsByTagName("ul");
	console.log(change2);
	for (const element of change2) {
		element.firstElementChild.style.display="none";
	}
	console.log("done");
//------------------4
	console.log("-------------------------------------4--------------------------------------------------");
	var change3=document.getElementsByTagName("li");
	console.log(change3);
	for (const element of change2) {
		if(element.innerText==="Pete"){
			element.style.border="solid black 1px"	
		}
	}
//------------------5
	console.log("-------------------------------------5--------------------------------------------------");
	var change4=document.body;
	change4.style.fontSize="40px";

//------------------6 Bonus
	console.log("-------------------------------------6--------------------------------------------------");
	//bcolor=
	if(change1.style.backgroundColor==="lightblue"){
		alert("Harold && admins");
		change1.textContent="Users: Harold && admins";
		console.log(change1);
	}
