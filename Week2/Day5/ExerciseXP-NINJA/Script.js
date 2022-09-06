//-------------------------------------------------------------------------The Hanging Game--------------------------------------------------------------------------
					function playTheGame(){								

								console.log("-------------Hanging Game------------");
								var word;
								do {
    									word= prompt("Player1 must Enter a minimum of 8 letters");
								} while (word.length<8);
								var player1= word.split("");
								var hiddenWord = "*".repeat(player1.length);
								var hidden = hiddenWord.split("");
								var apear;
								var player2,limit=0;
								alert("check the console")


								function Initi() {
									    for (const k in player1) {
										        if (player2 == player1[k]) {
										            hidden[k]=player1[k];
        										}
    										}
									    console.log(Apearent());
									    let ap = Apearent()
									    if (ap.indexOf("*") < 0) {
								  	          console.log("CONGRATS YOU WIN");	
										  alert("CONGRATS YOU WIN");
								  	          limit=11;
    										}
									    if (limit == 9) {
										        console.log("YOU LOSE");
											alert("YOU LOSE");
									    }
								}

								function Apearent() {
   									 apear = "";
    									for (i in hidden){
      									  apear = apear + hidden[i];
   									 }
    									return apear;
								}

							while (limit<10) {
    								player2= prompt("Player1 : Guess a letter");
    								Initi();
   								 limit++;
							}

						}
