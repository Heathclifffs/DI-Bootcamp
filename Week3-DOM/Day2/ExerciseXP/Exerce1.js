//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		console.log(document.body.firstElementChild.firstElementChild.textContent);
//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		document.body.firstElementChild.lastElementChild.outerHTML=" ";
		console.log(document.body.firstElementChild.lastElementChild);
//--------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		console.log(document.body.firstElementChild.firstElementChild.nextElementSibling);
		document.body.firstElementChild.firstElementChild.nextElementSibling.setAttribute("onclick","color()");	
		function color(){
			document.body.firstElementChild.firstElementChild.nextElementSibling.style.backgroundColor="red"
		}
//--------------------4
		console.log("-------------------------------------4--------------------------------------------------");
		console.log(document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling);
		document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.setAttribute("onclick","hider()");
		function hider(){
			document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.style.display="none"
		}
//--------------------5
		console.log("-------------------------------------5-------------------------------------------------");
		newbutton=document.createElement("button");
		console.log(newbutton);
		newbutton.textContent='click here to get all texts bold'
		newbutton.setAttribute("onclick","bolder()");
		function bolder(){
			document.body.style.fontWeight="bold"
		}
		document.body.appendChild(newbutton);
//--------------------Bonuses
		console.log("-------------------------------------6-------------------------------------------------");
		
		console.log(document.body.firstElementChild.firstElementChild);
		document.body.firstElementChild.firstElementChild.setAttribute("onmouseover","hooverr()")
		function hooverr(){
			var selected=Math.floor(Math.random() * 100);
			console.log(selected);
			document.body.firstElementChild.firstElementChild.style.fontSize=selected+"px";
		}
		document.body.appendChild(newbutton);

		console.log("-------------------------------------7-------------------------------------------------");
		console.log(document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling);
		var select=document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling;
		select.setAttribute("onmouseover","anims()")
		select.setAttribute('Class',"fade");
		sel=document.getElementsByClassName('fade');
		function anims(){
			select.setAttribute('Class',"fade");
			sel=document.getElementsByClassName('fade');
			//sel[0].style.opacity'0';
			select.style.opacity='1';
			select.style.transition='opacity 0.3s ease-in-out';
			//select.fade.style.opacity'0';
;
		}
		select.classList.toggle("fade")





























