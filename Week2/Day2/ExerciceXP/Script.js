			//------------------------------Exercise 1: ----------------------------------
						 //Simple If/Else Statement

							let x = 5;
    							let y = 7;

    					if (x>y) {
    						console.log('x is the biggest number' )
    						 }
    					     else{
    			       			 console.log('y is the biggest number')
    		    				}
			//---------------------------------------------Exercise 2-----------------------------------------------

								let newDog="Chihuahua";
							console.log(newDog.toUpperCase());
							console.log(newDog.toLowerCase());
							if( newDog==="Chihuahua"){
           								console.log('I love Chihuahua,it\'s my favorite dog breed')
							}else{
           								console.log('I don\'t  care ,I prefer cats')
								};


		//--------------------------------------------------Exercise3----------------------------------------------------
  						 let num=prompt("Entrez un nombre");
						   if((Number(num) % 2)==0){
   								alert(num+' is even');
									   }else{
   								alert(num+' is odd');
   										}


		//------------------------------------------------------ Exercise 4----------------------------------------------------		
					let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000","Nico16"];
					console.log(users[0],users[1] +" and "+users.slice(1).length + " more are online" );
