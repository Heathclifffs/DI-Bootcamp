var i=0;
var itter
function myMove(){
	console.log("you are here")
	itter=setInterval(anime,1);
}

function anime(){
	if(i<(document.body.children[1].scrollWidth-document.body.children[1].children[0].scrollWidth)){
		i=i+1;
		document.getElementById("animate").style.left=i+"px";
	}else{
		clears(itter)
	}
}
ss=document.body.children[1].scrollWidth
console.log(ss)
		function clears(itter){
			clearInterval(itter);
		}
		
