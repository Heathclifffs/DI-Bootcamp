//------------------2
	console.log("-------------------------------------2--------------------------------------------------");
	var change1=document.body.firstElementChild;
	console.log(change1);
	change1.setAttribute("id", "socialNetworkNavigation");
	console.log(change1);

//------------------3
	console.log("-------------------------------------3--------------------------------------------------");
	//------------------1
	newli = document.createElement('li');
	console.log(newli);
	//------------------2
	newTextNode = document.createTextNode('Logout');
	console.log(newTextNode);
	//------------------3
	newli.appendChild(newTextNode);
	console.log(newli);
	//------------------4
	select=document.body.firstElementChild.firstElementChild;
	console.log(select);
	select.appendChild(newli);
//------------------4 Bonuses
	console.log(select.firstElementChild.textContent);
	console.log(select.lastElementChild.textContent);
	alert(select.firstElementChild.textContent+" "+select.lastElementChild.textContent)
