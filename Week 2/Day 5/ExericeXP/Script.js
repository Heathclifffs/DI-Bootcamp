/* already do that in a C program
check html file for instructions 
*/
			function playTheGame(){
			//-------------------------------------------1st  Part----------------------------------------------------------------------------------------
					var result = confirm("Would you like to play this game");
            				if (result == true) {
			                		alert("OK was pressed.WELCOME ON MY JS GAME ");
							var numbers=2;
			//--------------------------------------------------------BONUS start-----------------------------------------------------------------------
						do{
							numbers=prompt("Enter a number between 0 and 10");
							numbers=parseInt(numbers);
							alert(numbers + " " +typeof(numbers));
							if(!numbers && numbers!==0) {
    								alert('Sorry Not a number, Goodbye XD')
  							} else if((typeof(numbers) === 'number') ||numbers==0) {
   								alert('Great the input is okay.Now let\'s check validity');
								if(numbers>=0 && numbers<=10){
										alert(numbers+' is  a valid number \n Now let the game begin are you ready ?')
										computerNumber=Math.floor(Math.random() * (+11 - +0)) + +0;
										alert('computerNumber chose with Success');
										// alert('computerNumber = '+computerNumber); checked 
										compareNumbers(numbers,computerNumber);

								}else{
									alert('Sorry it’s not a good number, Goodbye ...( you are funny guy XD)')
								}
  							}
			//--------------------------------------------------------BONUS end-----------------------------------------------------------------------
						}while((!numbers && numbers!==0) || (numbers < 0 || numbers > 10));
							
            				} else {
                					alert("Cancel was pressed. No problem, Goodbye");
            				}
				}

		//-----------------------------------------------------------part II----------------------------------------------------------------------------


			function compareNumbers(userNumber,computerNumber){
						var chance=3;
					while(chance!=0){
						if(userNumber === computerNumber ){
							alert('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WINNER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n The game will stop');
							chance=-1;
						}else if(userNumber > computerNumber){
							chance=chance-1;
							alert ('Your number is bigger then the computer’s, guess again \n left try again = '+chance);
						   do{
							userNumber=prompt('Enter an new valid value an restart !!!!');
							userNumber=parseInt(userNumber);
							alert(userNumber + " " +typeof(userNumber));
						   }while((!userNumber && userNumber !==0 )|| (userNumber < 0 || userNumber > 10));
	
						}else{
							chance=chance-1;
							 alert ('Your number is smaller then the computer’s, guess again \n left try again = '+chance);
						   do{
							userNumber=prompt('Enter an new valid value an restart !!!!');
							 userNumber=parseInt(userNumber);
							 alert(userNumber + " " +typeof(userNumber));
						   }while((!userNumber && userNumber !==0) ||(userNumber < 0 || userNumber > 10));
						}
					}
						if(chance===0){
							alert('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! LOSER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
						}
							
			}


















