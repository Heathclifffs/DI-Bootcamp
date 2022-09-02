		//-------------------------------------------------Exercise1---------------------------------------------------
						let langue=prompt("Enter the language you speak")
							let language=langue.toLowerCase();
							if (language=="french") {
								alert("Bonjour")
							}else if (language=="english") {	
								alert("Hello")
							}else if (language=="hebrew") {
								alert("Shalom")
							}else{
								alert("01110011 01101111 01110010 01110010 01111001")

							}




		// ------------------------------------------------Exercise2-------------------------------------------------------
						let grade=prompt("Enter your grade");
							if (grade>90) {
								console.log("A");
							}
							if (grade>80 && grade<=90) {
								console.log("B");
							}

							if (grade>=70 && grade<=80) {
								console.log("C");
							}

							if (grade<70) {
								console.log("D");
							}


		//-------------------------------------------------------------Exercise3----------------------------------------------------------------------------

								let verb=prompt("Enter a verbe please")
							if ( verb.length >= 3 &&  verb.slice(-3)!="ing"){
											console.log(verb+"ing");

							}else if ( verb.length >= 3 &&  verb.slice(-3)=="ing"){
											console.log(verb+"ly");

							}else{	console.log(verb);}


