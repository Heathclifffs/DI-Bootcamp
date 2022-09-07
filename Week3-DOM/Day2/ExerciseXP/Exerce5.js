//--------------------1
		console.log("-------------------------------------click--------------------------------------------------");
		document.body.children[0].addEventListener("click",function(){
				Default()
		});
function Default(){
	document.body.children[0].style.fontSize="12px";
	document.body.children[0].style.backgroundColor="black";
	document.body.style.backgroundColor="gray";
	document.body.children[0].style.color="white"
}
console.log("-------------------------------------dblclick--------------------------------------------------");
	document.body.children[0].setAttribute('ondblclick','change1()')
	document.body.children[0].setAttribute("mouseover","nochange()")
	document.body.children[0].setAttribute("mouseout","change2()")

	function change1(){
		document.body.children[0].style.fontSize="100px";
		document.body.children[0].style.backgroundColor="red";
		document.body.style.backgroundColor="orange";
		document.body.children[0].style.color="white"
	}
console.log("-------------------------------------mouseout--------------------------------------------------");
function change2(){
		document.body.children[0].style.border="solid black 3px";
		document.body.children[0].style.backgroundColor="blue";
		document.body.style.backgroundColor="yellow";
		document.body.children[0].style.color="white"
	}
console.log("-------------------------------------mouseover--------------------------------------------------");
function nochange(){
		document.body.children[0].style.fontSize="70px";
		document.body.children[0].style.backgroundColor="red";
		document.body.style.backgroundColor="orange";
		document.body.children[0].style.color="white"
	}
