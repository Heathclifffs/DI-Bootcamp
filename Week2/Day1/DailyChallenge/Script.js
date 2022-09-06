// Exercise 1

		
		let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
		fruits.shift();
		// sort array in  alphabetical order
		fruits.sort();
		fruits.push("Kiwi");
		fruits.splice(0,1);
		fruits.reverse();
		console.log(fruits);


// Exercise 2


		let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
        console.log(moreFruits[1][1]);
