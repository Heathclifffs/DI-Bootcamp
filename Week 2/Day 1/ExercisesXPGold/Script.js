//Exercise 1


let sentence = ["my","favorite","color","is","blue"];
   

   //Write some simple Javascript code that will join all the items in the array above, and console.log the result.

    console.log(sentence.join());
    //or second method
    console.log(sentence.toString());
    console.log(sentence.join(' '));

    
//Exercise2
		//1

		let str1 = "mix";
		let str2 = "pod";

		//2


        let temp = str1;
		console.log(str2.slice(0,2)+ str1.substring(2,3));
		console.log(str1.substring(0,2) + str2.substring(2,3));
		
		
		
		//3
		temp=str1 + " "+str2
		console.log(temp)

//Exercise3
		


		//1
		let num1=prompt('Entrez la premiere valeur')
		//  to convert num1 to a number we'll use the Number() methode;
		let num2=prompt('Entrez la deuxieme valeur');
		

		
//Bonus

	let operator=prompt('which operation wish you make type \n \
		                 \'1\' for addition \n \
                         \'2\' for substraction \n \
                         \'3\' for multiplication \n \
                         \'4\' for division  ');

 switch(operator){

   	case '1' :
     	alert("result= " + (Number(num1)+Number(num2)));
    	break;     

   	
   	case '2' :
    	alert("result= " + (Number(num1)-Number(num2)));
   	    break;

   	case '3' :
    	alert("result= " + (Number(num1)*Number(num2)));
   		break;
   	
   	default:
    	alert("unvalid operator");
    	break;
   } 
