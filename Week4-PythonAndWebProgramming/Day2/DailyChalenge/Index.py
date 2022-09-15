''' Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
'''
print ('#--------------------------------------------------- Challenge 1')
number=int(input('Enter a number: '))
loop=int(input('Enter a length: '))
multiple=[]
j=1
for i in range(loop):
	multiple.append((number*j))
	j=j+1

print(f"{number} - length : {loop} -> ",end='')
for i in multiple:
	print(i," ",end='')	

''' Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
'''
print('\n')
print ('#--------------------------------------------------- Challenge 2')

userword=input('enter your word : ')
lis=['passing','lottery','add','all','app','ass','bee','boo','coo','ebb','eel','egg','ell','err','fee','foo','goo','hee','hmm','ill','inn','lee','nee','odd','off']
l=[]
l.append(userword[0])
if(userword in lis) :
	print("the correct word = ",userword)
elif(len(userword)==1):
	print("the correct word = ",userword)
else:
	for i in range(1,len(userword)) :
		word1=userword[i-1]
		word2=userword[i]
		print(word1,"",word2)
		if(word1==word2):
			print('double find')
		else:
			l.append(word2)
	userword=''.join(l)
	print("the correct word = ",userword)















			


