//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		var allBoldItems=[]
//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		//console.log( document.getElementsByTagName("strong"));
		function getBold_items(){
			var select=document.getElementsByTagName("strong");
			console.log(select);
			i=-1;
			for (const element of select) {
				i=i+1;
				allBoldItems[i]=element;
			}
			console.log(allBoldItems);
		}
		getBold_items()
//--------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		function highlight(){
			for (const elements of allBoldItems) {
			 	 elements.style.color="blue";
			}
		}
//--------------------4
		console.log("-------------------------------------4--------------------------------------------------");
		function return_normal(){
			for (const elements of allBoldItems) {
			 	 elements.style.color="black";
			}
		}
//--------------------5
		console.log("-------------------------------------5--------------------------------------------------");
		var changer=document.body.children[0]
		changer.setAttribute("onmouseover","highlight()");
		changer.setAttribute("onmouseout","return_normal()");
		console.log(changer);


//highlight()
