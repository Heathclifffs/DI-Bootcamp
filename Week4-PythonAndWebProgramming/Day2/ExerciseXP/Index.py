# -------------------------------------------------------- Exercise 1 : Set
print ('#---------------------------------------------------Exercise 1 : Set')
my_fav_numbers=[1,12,6,20,21,7,60,0]
print('my fav numbers = \t',end='')
for n in my_fav_numbers:
	print(n," ",end='')
print('\n')
for i in range(2):
	new=int(input(f'\tinput the {i+1}e new fav number: \t'))
	my_fav_numbers.append(new)
print('my fav numbers are now = \t',end='')
for n in my_fav_numbers:
	print(n," ",end='')
print('\n')
new=my_fav_numbers[-1]
print(f'\nthe last {new} will be remove');
my_fav_numbers.remove(new)
for n in my_fav_numbers:
	print(n," " ,end='')
friend_fav_numbers=[2,13,7,19,18,4]
print('\n')
print('my friend  fav numbers = \t',end='')
print('')
for n in friend_fav_numbers:
	print(n," ",end='')
our_fav_numbers=my_fav_numbers+friend_fav_numbers
print('\n')
print('So our fav numbers are :',end='')
for n in our_fav_numbers:
	print(n," ",end='')
# ---------------------------------------------------------------- Exercise 2: Tuple
print('\n')
print('# ------------------------------------------------------------ Exercise 2: Tuple')
mytuple=(1,2,3,4,5,6,7,8,9,0)
print('values in my tuple are :\t ',end='')
for n in mytuple:
	print(n,' ',end='')

print ('\n')
print('A tuple is a collection which is ordered and unchangeable.so no we can\'t add anything to it ')

# ---------------------------------------------------------------- Exercise 3: List
print('\n')
print('# ------------------------------------------------------------ Exercise 3: List')
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print('for now there are in my bucket : ',end='')
for item in basket:
	print(item,' ',end='')

print('\n')
for item in basket:
	if(item=="Banana"):
		print(item," is find now removing it")
		basket.remove(item)
		print(item," removing done")

for item in basket:
	if(item=="Blueberries"):
		print(item," is find now removing it")
		basket.remove(item)
		print(item," removing done")
print('\n')
print('Now there are in my bucket : ',end='')
for item in basket:
	print(item," ",end='')

print('\n')
print('adding of new element in basket')
basket.append("Kiwi")
basket.insert(1,"Apples")
for item in basket:
	print(item," ",end='')

print('\n')
count=0
for item in basket:
	if(item=="Apples"):
		print('an',item," is find")
		count=count+1
print(f'there are {count} Apples in my bucket')
basket.clear()
print('the empty basket = ',basket)

# ---------------------------------------------------------------- Exercise 4: Floats
print('\n')
print('# ------------------------------------------------------------ Exercise 4: Floats')
print(' 1-------- a floating-point or float is a variable type that is used to store floating-point number values. A floating-point number is one where the position of the decimal point can "float" rather than being in a fixed position within a number')
print('2------ by using random.uniform and couping with a loop')
var=1
let=1
thelist=[]
for i in range(10):
	if(let==1):
		thelist.append(int(var))
		var=var+0.5
		let=0
	else :
		thelist.append(var)
		var=var+0.5
		let=1
for item in thelist:
	print(item," ",end='')


# ---------------------------------------------------------------- Exercise 5: For Loop
print('\n')
print('# ------------------------------------------------------------Exercise 5: For Loop')
print('display of all numbers from 1 to 20')
for i in range (1,21):
	print(i," ",end='')
print('\n')
print('display of even numbers from 1 to 20')
for i in range (1,21):
	if ((i%2)==0):
		print(i," ",end='')



# ---------------------------------------------------------------- Exercise 6 : While Loop
print('\n')
print('# ------------------------------------------------------------Exercise 6 : While Loop')
myname='Harold'
yourname=''
while(yourname != myname) :
	print('Rule: i\'m Harold and your name must be equal to mine to left the loop ')
	yourname=input('input your name please:\t')



# ---------------------------------------------------------------- Exercise 7: Favorite Fruits
print('\n')
print('# ------------------------------------------------------------Exercise 7: Favorite Fruits')
print('separate the fruits with a single space')
fruits=input('what are your favorites fruits :\t')
thelist=fruits.split(" ")
for item in thelist:
	print(item," ",end='')

print("\n")
choice=input("Enter a fruit:\n")
if choice in thelist:
	print("You chose one of your favorite fruits! Enjoy!")
else :
	print("You chose a new fruit. I hope you enjoy")



# ---------------------------------------------------------------- Exercise 8: Who Ordered A Pizza ?
print('\n')
print('# ------------------------------------------------------------Exercise 8: Who Ordered A Pizza ?')
toppings=[]
topping=''
prize=10
while( topping !="quit"):
	topping=input('enter a topping or quit to quit : ')
	if(topping!='quit') :
		toppings.append(topping)
		print(f"We’ll add that {topping} to your pizza.")
		prize=prize+2.5
	else :
		print('Your troppings are :\t',end='')
		for i in toppings:
			print(i," ",end='')
		print('\n')
		print("Bill =",prize)



# ---------------------------------------------------------------- Exercise 9: Cinemax
print('\n')
print('# ------------------------------------------------------------Exercise 9: Cinemax')
name=['Harold','Nicodeme','Mary', 'Jeanne']
number=int(input('how many are you ?'))
bill=0
for i in range(number):
	age=int(input((f'how old is the {i+1}e person ?')))
	if(age<3):
		bill=bill+0
	elif (age>=3 and age<=12) :
		bill=bill+10
	elif(age>12):
		bill=bill+15
	else:
		print('you are not repertoried')

print('Bill = ',bill)
final=[]
for i in name:
	age=int(input((f'how old is {i} ')))
	if(age>=16):
		final.append(i)
	else:
		print('you are not allowed to see watch this movie')

print('Those who are allow to see this movie are : ',end='')
for i in final:
	print(i," ",end='')



# ---------------------------------------------------------------- Exercise 10 : Sandwich Orders
print('\n')
print('# ------------------------------------------------------------Exercise 10 : Sandwich Orders')
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
print("we are starting to prepare your sandwich")
for i in sandwich_orders :
	finished_sandwiches.append(i)
	print(f'I made your {i}')
# ---------------------------------------------------------------- Exercise 11 : Sandwich Orders#2
print('\n')
finished_sandwiches=[]
print('# ------------------------------------------------------------Exercise 11 : Sandwich Orders#2')
sandwich_orders = ["Tuna sandwich","Pastrami sandwich","Avocado sandwich","Pastrami sandwich","Egg sandwich","Pastrami sandwich","Sabih sandwich","Pastrami sandwich"]
print('we are running out of  pastrami')
for i in sandwich_orders :
	if (i=="Pastrami sandwich"):
		print('we are running out of  pastrami')
	else:
		finished_sandwiches.append(i)
		print(f'I made your {i}')














































































