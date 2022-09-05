//---------------------------------------------------------------------- Exercise 1 --------------------------------------------------------------------------------

						    let obj1 = {
						    FullName : "Azien SOSUKE",
						    Mass : 80,
						    Height : 1.90,
						    BMI : function () {
        					   return this.Mass/(this.Height * this.Height);
    						   }
}
						   let obj2 = {
						    FullName : "Gon FREEGS",
   						    Mass : 50,
    						   Height : 1.50,
    						  BMI : function () {
					        return this.Mass/(this.Height * this.Height);
    						}
					}

					function compareBMI(ob1,ob2) {
    							if (ob1.BMI() > ob2.BMI()) {
							        console.log(ob1.FullName+" have the largest BMI: "+ob1.BMI())
						       } else{
							        console.log(ob2.FullName+" has the largest BMI: "+ob2.BMI())
    							}
					}

					compareBMI(obj1,obj2);

//---------------------------------------------------------------------Exercise 2 ---------------------------------------------------------------------------------


				function findAvg(gradesList) {
  					 let average=0;
                 	                 for (const i of gradesList) {
					        average=average+i;
					 }
				        decision(average=average/gradesList.length);
				}


				function decision(params) {
				    if (params>65) {
				       console.log(params+" : You passed")
				    } else{
				        console.log(params+" : You failed and must repeat the course.")
    					}
				}

				findAvg([44,10,67,75,70]);
