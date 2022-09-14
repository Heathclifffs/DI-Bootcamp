			newinput=document.createElement("input");
			newinput.setAttribute("placeholder","input only letters please");
			newinput.setAttribute("type","text");
			newinput.setAttribute("name","text");
			newinput.setAttribute("onkeydown","check()");
			newinput.addEventListener("click",function(event){
				event.preventDefault()
			});
			document.body.appendChild(newinput);
			
			function check(){
				tab=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
				console.log(tab)
				var select=document.body.children[1];
				var checked=false;
				console.log(select)
				console.log(select.value)
				var i=select.value.substring(select.value.length-1,select.value.length);
				console.log(i)
				for (const elements of tab) {
					if(elements===i || elements.toUpperCase() ===i ){
				 		 checked=true;
						console.log(checked)
					}
				}
				if(checked===false){
					select.value=select.value.substring(0,select.value.length-1);
				}
			}
