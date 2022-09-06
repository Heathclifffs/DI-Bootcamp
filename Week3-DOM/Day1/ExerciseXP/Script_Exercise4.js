//--------------------1
		console.log("-------------------------------------1--------------------------------------------------");
		newdiv = document.createElement('div');
		newdiv.setAttribute("class", "listBooks");
		console.log(newdiv);
		document.body.appendChild(newdiv)

//--------------------2
		console.log("-------------------------------------2--------------------------------------------------");
		var book= new Object();
			
			book.title=" ";
			book.author=" "
			book.image=" ";
			book.alreadyRead=0;
			
		
		//};
		var allBooks=[];
		console.log(book);
		console.log(allBooks);
		var books=[];
//--------------------3
		console.log("-------------------------------------3--------------------------------------------------");
		for(var i=0;i<2;i++){
			books[i]=new Object;
			books[i].title=prompt("input the title of the book "+(i+1)+"");
			console.log(books[i].title);
			books[i].author=prompt("input the author of the book "+(i+1)+"");
			console.log(books[i].author);
			books[i].image=prompt("input the url of image of the book "+(i+1)+"");
			console.log(books[i].title);
			do{
			books[i].alreadyRead=prompt("do you already Read the book "+(i+1)+" ?\nType: 1-Yes\t\t 2-No");
			books[i].alreadyRead=parseInt(books[i].alreadyRead);
			console.log(typeof(books[i].alreadyRead)+books[i].alreadyRead);
			console.log(books[i].alreadyRead);
			}while(!books[i].alreadyRead ||(books[i].alreadyRead!==2 && books[i].alreadyRead!==1));
			allBooks[i]=books[i];
			console.log(allBooks);

		}

//--------------------4
		console.log("-------------------------------------4------------------------------------------------------------------------------");
		newp=[];
		newimg=[];
		newTextNode=[];
		for (var j=0;j<2;j++){
			newp[j] = document.createElement('p');
			console.log(newp[j]);
			newimg[j] = document.createElement('img');
			newimg[j].setAttribute("src",allBooks[j].image);
			newimg[j].setAttribute("width","100px");
			console.log(newimg[j]);
			newTextNode[j] = document.createTextNode(" "+allBooks[j].title+" written by "+allBooks[j].author+" ");
			console.log(newTextNode[j]);
			newp[j].appendChild(newimg[j]);
			console.log(newp[j]);
			newp[j].appendChild(newTextNode[j]);
			console.log(newp[j]);
			document.body.firstElementChild.nextElementSibling.appendChild(newp[j])
			if(allBooks[j].alreadyRead===1){
				newp[j].style.color="red";
			}
			
		}
		
	
