					//-------------------------Exercise 1 Code----------------------------------------

		 	  	 favoriteFood="Cake";
		 	  	 favoriteMeal="Diner";
		 	  	 console.log("I eat " +favoriteFood + " at every " + favoriteMeal);

	
					//--------------------------Exercise 2 Code-------------------------------------

			//Part1
			 	 myWatchedSeries = ["Supernatural", "Psych", "Bungo Stray Dog"];
			  	 myWatchedSeriesLength=myWatchedSeries.length;
			  	 myWatchedSeriesSentence=myWatchedSeries.toString();
			  	 console.log("I watched 3 series : "+ myWatchedSeriesSentence );

	    		//Part2	

	    	       		  myWatchedSeries.splice(2,1,"friends");
			    	  myWatchedSeries.push("Crisis");
	    			  myWatchedSeries.unshift("Lord Of Rings");
	    			  myWatchedSeries.splice(1,1);
	    			  console.log(myWatchedSeries[1].substring(2,3));
	    			  console.log(myWatchedSeries) 
	      			  


		//-----------------------------------------------------------Exercise3 Code------------------------------------------------------------------------------


									celsiusTemperature=35;
					//2-we don't need to create another variable to hold the temperature in fahrenheit
	   				 console.log(celsiusTemperature +" °C"+" is " +(celsiusTemperature/5*9+32));






		//------------------------------------------------------------Execise4 Code---------------------------------------------------------------------------------------

  							let c;
    							let a = 34;
   							let b = 21;
					console.log(a+b) //first expression
    		//Prediction: 55 because 34 and 21 are respectivly the values of a and b and we add 21 to 34 the result is 55
    							// Actual:55

    							a = 2;

    					console.log(a+b) //second expression
   			 // Prediction:23 because the a value's change and is 2 now when we add  21 to 2 we got 23
    							// Actual:23



							//1-yes it will be an outcome|outcome:55
							//2-yes it will be an outcome|outcome:23 
							/*3-The value of c is null*/console.log(c);
						   //Analyse the code below, what will be the outcome?
					  /*console.log(3 + 4 + '5') outcome will be 75*/console.log(3 + 4 + '5');




		//----------------------------------------------------------------Exercise5 Code-----------------------------------------------------------------------------------------------------


 										typeof(15)
							    // Prediction:integer because 15 is an integer
								console.log(typeof(15));// Actual:number
										typeof(5.5)
							   // Prediction:number because 5.5 is a number
								console.log(typeof(5.5));// Actual:number

										typeof(NaN)
							   // Prediction:not a number
								console.log(typeof(NaN));// Actual:number
										typeof("hello")
							   // Prediction:string because hello is between quotes 
							     console.log(typeof("hello"));// Actual: string

										typeof(true)
							   // Prediction: boolean because true is a boolean value
							      console.log(typeof(true));// Actual:boolean

										typeof(1 != 2)
					   // Prediction:boolean cause 1 !=2 is a comparison and it will return true or false
								console.log(typeof(1 != 2));// Actual:boolean
									"hamburger" + "s"
						// Prediction: hamburgers because it is a concat method , Actual: humburgers
									"hamburgers" - "s"
				// Prediction: hamburger because like a "+"operator it should substract the s to hamburgers Actual:NaN
										"1" + "3"
						// Prediction:13 because it is a concat operation , Actual:13
										"1" - "3"
						// Prediction:NaN error because we are doing math not number , Actual:NaN
										"johnny" + 5
							// Prediction:concat jonnhy5 , Actual:johnny5
										"johnny" - 5
							// Prediction:NaN because johnny is not a number , Actual:NaN
										99* "hello"
							// Prediction:NaN because "hello" is not number , Actual:NaN
										1 != 1
						// Prediction:false because it is a comparison and 1 !=1 is false , Actual: false
										1 == "1"
						// Prediction: true because 1=1 , Actual:true

										1 === "1"
				// Prediction:false because === will compare also the type of arguments "1" and 1 and they don't matche
 
										// Actual:false



	//------------------------------------------------------------------Exercise6 Code---------------------------------------------------------------------------


										5 + "34"
							// Prediction:534
							// Actual:534

										5 - "4"
								// Prediction:NaN  because "34" isn't a number
										// Actual:1

										10 % 5
						// Prediction:0 
								// Actual:0

									5 % 10
						// Prediction: 5
						// Actual:5

								"Java" + "Script"
					// Prediction:'JavaScript'
							// Actual:JavaScript

									" " + " "
				// Prediction:"  "
						// Actual:'  '

						" " + 0
		// Prediction:" 0"
 		// Actual:' 0'

				true + true
		// Prediction: 1 
			// Actual:1

 				true + false
	// Prediction:1  because true = 1 and false =0 so true + false give 1
	// Actual:1

				false + true
	// Prediction:1 because true = 1 and false =0 so true + false give 1
			// Actual:1

			false - true
		// Prediction: -1 because true = 1 and false =0 so false + true give  -1
			// Actual:

						!true
			// Prediction: false because not true is  false
						// Actual:false

						3 - 4
				// Prediction:-1 
				// Actual:-1

					"Bob" - "bill"
			// Prediction:NaN 
			// Actual: NaN





