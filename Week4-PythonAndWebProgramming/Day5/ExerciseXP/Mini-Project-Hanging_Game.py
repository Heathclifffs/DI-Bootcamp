#-------------------------------------------------------------------------The Hanging Game--------------------------------------------------------------------------
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
def playTheGame():								

	print("-------------Hanging Game------------");
	print('list of words')
	print(wordslist)
	uword=input('choose a word :')
	while(uword not in wordslist):
		uword=input('word must be in the list so choose a word :')
	hiddenWord = "*"*len(word)
	print(hiddenWord)
	hidden = word.split("");
playTheGame()
'''var apear;
								var player2,limit=0;
								alert("check the console")


								function Initi() {
									    for (const k in player1) {
										        if (player2 == player1[k]) {
										            hidden[k]=player1[k];
        										}
    										}
									    print(Apearent());
									    let ap = Apearent()
									    if (ap.indexOf("*") < 0) {
								  	          print("CONGRATS YOU WIN");	
										  alert("CONGRATS YOU WIN");
								  	          limit=11;
    										}
									    if (limit == 9) {
										        print("YOU LOSE");
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
'''
