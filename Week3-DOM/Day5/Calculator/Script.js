						//document.getElementById("result").innerHTML=equal();
//----------------------------------------------------------------The equal Function-----------------------------------------------------------------------------------
						
						
						function equal(){
							let var1 = document.getElementById("result").innerHTML; 
             						let var2 = eval(var1) ;
             						document.getElementById("result").innerHTML = var2; 
							
						}


//-------------------------------------------------------------------The number Function-------------------------------------------------------------------------------

						function number(numbers){
							document.getElementById("result").innerHTML+=numbers;
						}


//-------------------------------------------------------------------The operator Function-------------------------------------------------------------------------------

						function operator(op){
							document.getElementById("result").innerHTML+=op;

						}

//--------------------------------------------------------------------------The reset Function-------------------------------------------------------------------------

						function reset(){
							document.getElementById("result").innerHTML=" ";

						}
//--------------------------------------------------------------------------The clear Function-------------------------------------------------------------------------

						function clears(){
							let len = document.getElementById("result").innerHTML;
							let len2=len.length;
							len=len.substring(0,len2-1);
							document.getElementById("result").innerHTML=len;
						}
