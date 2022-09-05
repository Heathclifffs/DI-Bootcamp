//----------------------------------------------------------------------------Execise 1----------------------------------------------------------------------------
	
								//-------------Part 1---------------
			
							let people = ["Greg", "Mary", "Devon", "James"];
										
								//1
								people.shift();
								console.log(people);
								//2
								people.splice(2,1, "Jason");
								//3
								people.push("Harold");
								//4
								console.log(people.indexOf("Mary"))
								//5
								console.log(people.slice(1,3));
								//6
								console.log(people.indexOf("foo"))
						// indexOf("Foo") return -1 because "foo" is not exist in the array
								//7
								let last=people.slice(3);
								console.log(last)
								console.log(people.indexOf("Nicodeme"))
							// the relation is that indexof (last) element equal to length of the array -1
								console.log(people);

	
								//-------------------Part 2---------------------

			
								//1
								for(let i in people){
			
									console.log("."+people[i])
									}
	
								//2
								for(let i in people){
									if (people[i]=="Jason") {
											break;
										}
									console.log("."+people[i])
								}

			
			
			
//------------------------------------------------------------------------Exercise 2------------------------------------------------------------------------------------
   
  						 let colors=['Black','Gray', 'Blue','Orange' ,'White'];
   						 let first=['st','nd','rd','th','th'];
						 for(var i in colors ){
						function favorite() {
							 return ( colors.indexOf(colors[i])+1);
			  			}
						console.log("My #"+ favorite()+first[i]+" choice is " + colors[i])
						}


//----------------------------------------------------------------------------Exercise 3--------------------------------------------------------------------------------
								//1
								let number=prompt("Enter a number please");
								while(Number(number)<10){
								alert("Enter a new number the actual is low than what required")
								number=prompt("Enter a number please");
								}
			//simple While loop is more relevant in this case because it will always check the first answer of the user before giving an answer
				
				
//--------------------------------------------------------------------------------Exercise4----------------------------------------------------------------------------
		
									//1			
									let building = {
										    numberOfFloors : 4,
										    numberOfAptByFloor : {
									            firstFloor : 3,
        									    secondFloor : 4,
									            thirdFloor : 9,
        									    fourthFloor : 2,
  										  },
   									 nameOfTenants : ["Sarah", "Dan", "David"],
   									 numberOfRoomsAndRent:  {
       											 sarah: [3, 990],
        										 dan :  [4, 1000],
        										 david : [1, 500],
										    },
										}		
       								  //2
								  console.log(building.numberOfFloors)		
	      							//3
							   console.log("There are"+building.numberOfAptByFloor.firstFloor+" at the first floor and "+building.numberOfAptByFloor.thirdFloor+" at the third");
         							//4
							         console.log("The second tenant is "+ building.nameOfTenants[1]+ " has "+ building.numberOfRoomsAndRent.dan[0]+" rooms in his apartement");
								// 5
								let sumrentDaSa=building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1];
								let rentdan=building.numberOfRoomsAndRent.dan[1]
								if(sumrentDaSa>rentdan){
								rentdan=rentdan+200;
								}
								console.log(rentdan)
				
				
				
//-------------------------------------------------------------------------------Exercise5----------------------------------------------------------------

						//1
						let familly={
							lastname  : "BASSOLE",
							Adresse :"25",
							numberOfmembers :7
							}
						//2
						for (i in familly){
								console.log(i);
	
								}
						//3
						for (i in familly){
							console.log(familly[i]);
	
								}


//------------------------------------------------------------------------------------Exercise6--------------------------------------------------------------------

								let details = {
 										 my: 'name',
 										 is: 'Rudolf',
  										the: 'raindeer'
									}
								//1
								let sentence=[];

								for ( let i in details){
	
									sentence.push(i+" "+details[i]);

									}

								console.log(sentence.join(""));



//---------------------------------------------------------------------------------------Exercise7----------------------------------------------------------------------

						let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
	
							names.sort();
							let society=[];
							for(i in names){
							society.push(names[i].slice(0,1));
			
							}
			
							console.log(society.join(""));
		
