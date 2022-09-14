//------------------------------------------------ Todo list
				var listTasks = [];
				var form=document.body.children[0].children[1];
				var valeur;
				console.log(form);
				function addTask(){
					document.getElementById("add").addEventListener("click",function(event){
					  event.preventDefault();
				        valeur=document.getElementById("text").value;
				        	if(valeur===""){
					        	alert("invalid task");
					        }else{
					           newinput=document.createElement('input')
						   newinput.setAttribute('type','checkbox')
						   newp=document.createElement('p')
						   newtext=document.createTextNode(valeur)
						   newp.appendChild(newinput)
						   newp.appendChild(newtext)
						   document.body.children[0].children[2].appendChild(newp)
		
        					}
    					});
    
				};
		addTask();
function endTask(){
	listTasks=document.getElementsByTagName("input")
	console.log(listTasks);
	for(const e of listTasks){
		if(e.type==='checkbox' && e.checked===true){
			e.parentElement.style.textDecoration="line-through"
		}else{
			e.parentElement.style.textDecoration="none"
		}
	}
}
setInterval(endTask,100);
