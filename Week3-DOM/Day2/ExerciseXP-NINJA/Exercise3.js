var locate=document.getElementById("result");
function geo(){
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition,showError);
	}else{
		locate.innerHTML="Geolocation is not supported on this browser update it"	
	}
	function showPosition(position){
		locate.innerHTML="Latitude:"+ position.coords.latitude+"<br>Longitude:"+position.coords.longitude;
	}
	function showError(error){
		switch(error.code){
			case error.PERMISSION_DENIED:
				locate.innerHTML="locate denied by user."
				break;
			case error.POSITION_UNAVAILABLE:
				locate.innerHTML="locate info is unavailable."
				break;
			case error.TIMEOUT:
				locate.innerHTML="TimeOUT"
				break;
			case error.UNKNOWN_ERROR:
				locate.innerHTML="Unknown error occur"	
		}
	}
}
