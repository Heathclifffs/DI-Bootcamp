					let words=prompt("Enter several words separated by commas");
					let liste=words.split(",");
					let max=0;
					for(let mot of liste ){
							if (mot.length > max){
							max=mot.length;
							}

						}
				//Hello, World, in, a, frame
	
				max=max+4;
				let starsOrWords="";
				console.log(starsOrWords.padStart(max,"*"));

				for(let mot of liste){
				let reste=max-(2+mot.length)-1;


				console.log("".padStart(2,"* ")+mot+"".padEnd(reste," ")+"".padEnd(1,"*"));
				}



				console.log(starsOrWords.padStart(max,"*"));

