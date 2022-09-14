		var tab=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		newdiv=document.createElement("div");
		newdiv.style.width="100%";
		newdiv.style.height="90vh";
		newdiv.style.display="inline-block";
		newdiv.setAttribute("id","content");
		newdiv.style.textAlign="center";
		var changer=document.body
		changer.style.height="99vh"
		changer.appendChild(newdiv);
		for (const elements of tab) {
			newdiv1=document.createElement("div");
			newdiv1.setAttribute("id","boxes"+elements);
			newText= document.createTextNode(elements.toUpperCase()+elements);
			newdiv1.appendChild(newText);
			newdiv1.setAttribute('ondragstart','dragStart(event)');
			newdiv1.setAttribute('ondragend','dragDrop(event)');
			newdiv1.setAttribute('draggable','true')
			newdiv1.style.width="2.4%";
			newdiv1.style.display="inline-block";
			newdiv1.style.textAlign="center";
			newdiv1.style.marginLeft="1.1%";
			newdiv1.style.border="solid black 1px";
			changer.children[1].appendChild(newdiv1);
				
		}
	
	function dragStart(event) {
		  event.target.style.backgroundColor = "lightpink";
  		  console.log ("drag " +  "X: " + event.clientX  + " Y: " +  event.clientY);
	}
	function dragDrop(event) {
		event.target.style.backgroundColor = "lightgreen";
    		var x = event.clientX;
		x=Math.abs(x)
    		var y = event.clientY;
		y=Math.abs(y)
		console.log(x)
		console.log(event.clientX)
    		console.log(event)
    		event.target.style.left = x + "px";
    		event.target.style.top = y + "px";
    		event.target.style.position = "absolute"; //Necessary
    		console.log ("dragend" + "X: " + event.clientX  + " Y: " +  event.clientY );
 
	}


//console.log(changer.children[1])


