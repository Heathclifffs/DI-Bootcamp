let sentence ="The movie is not that bad, I like it";
let wordNot =sentence.indexOf("not");
console.log(wordNot);
let wordBad =sentence.indexOf("bad");
if(wordNot<wordBad && wordNot>0 &&wordBad>0){
console.log(sentence.slice(0,wordNot)+"good"+sentence.slice((wordBad+3)));

}
else{
	console.log(sentence);
}
