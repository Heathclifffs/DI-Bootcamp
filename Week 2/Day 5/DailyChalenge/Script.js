		function playTheSong(){
				alert('The lyrics Will be Show up ');
			do{
				var numbers = prompt('How many bottle do you Have ?????');
				numbers=parseInt(numbers);
				alert('your Number : '+ numbers + " " + typeof(numbers));
				if(!numbers && numbers !== 0){
					alert('that\'s not a number \n enter a valid input');			
				}else{
						alert(numbers+' Bottles Of Beer Lyrics\n\n We start the song at '+numbers+' bottles' );
						var oNumber=0;
						var cmp=numbers;
						while(cmp >0){
							oNumber=oNumber+1;
							cmp=cmp-oNumber;
							if(oNumber===1){
								alert('Take '+ oNumber+ ' down, pass it around \nwe have now '+ cmp +' bottles');
							}else if(cmp===1 ||cmp===0){
								alert('Take '+ oNumber+ ' down, pass them around \nwe have now '+ cmp +' bottle');
							}else if((cmp-oNumber)<0){
								alert('no bottle of beer on the wall');
								break;				
							}else{
								alert('Take '+ oNumber+ ' down, pass them around \nwe have now '+ cmp +' bottles');
							}
						}
					}
			}while(!numbers && numbers !== 0);
		}
