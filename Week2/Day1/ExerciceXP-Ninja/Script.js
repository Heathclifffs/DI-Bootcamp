//Exercise1


	5 >= 1
//Prediction:True cause 5 est superieur a 1
//Actual:true
    0 === 1
    //Prediction:false parce que 0 est different de 1
//Actual:false
    4 <= 1
    //Prediction:false parce que 4 est superieur a 1
//Actual:false
    1 != 1
    //Prediction:false parce que 1 est egale a 1
//Actual:false
    "A" > "B"
    //Prediction: false parce que A est inferieur a B dans la table ascii
//Actual:false
    "B" < "C"
    //Prediction: true parce que B est inferieur a C dans la table ascii
//Actual:true
    "a" > "A"
    //Prediction:false parce que a est inferieur a A dans la table ascii 
//Actual:true
    "b" < "A"
    //Prediction:true 
//Actual:true
    true === false
    //Prediction: false parce que true est different de false
//Actual:false
    true != true
    //Prediction: false parce que true = true
//Actual:true



//Exercise2
let numbers=prompt('Enter string of numbers separated by commas eg:"2,3"');
let num=numbers.split();
let numsum=num.join('+');
console.log(numsum)
console.log(Number(numsum));
