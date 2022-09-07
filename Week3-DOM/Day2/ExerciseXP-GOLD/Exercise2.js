//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		console.log(document.getElementById("colorSelect").nextElementSibling);
		var select1=document.getElementById("colorSelect").nextElementSibling;
		select1.setAttribute("onclick","removecolor()")
		function removecolor(){
			select2=document.getElementById("colorSelect").value;
			console.log(select2);
			var Aray=document.getElementsByTagName("option");
			for (const elements of Aray ) {
				//console.log(elements);
				if(elements.textContent===select2){
					elements.outerHTML="";	
				}
				
			}
		}
