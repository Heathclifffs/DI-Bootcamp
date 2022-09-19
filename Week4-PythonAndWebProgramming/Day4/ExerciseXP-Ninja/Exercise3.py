
# ----------------------------------------------- Exercise 3 : Box Of Stars
'''  Instructions
  Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
  For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
  ******************
  * Hello          *
  * World          *
  * in             *
  * reallylongword *
  * a              *
  * frame          *
  ******************
'''
def box_printer(word1,word2,word3,word4,word5):
	lists=[len(word1),len(word2),len(word3),len(word4),len(word5)]
	lis=[word1,word2,word3,word4,word5]
	maxs=max(lists)
	for i in range (maxs+2):
		print('*',end='')
	print('**')
	for e in lis:
		print(f'*{e}',end='')
		for j in range((maxs+2)-len(e)):
			print(' ',end='')
		print('*')
	for i in range (maxs+2):
		print('*',end='')
	print('**')

word1=input("enter word 1 : ")
word2=input("enter word 2 : ")
word3=input("enter word 3 : ")
word4=input("enter word 4 : ")
word5=input("enter word 5 : ")
box_printer(word1,word2,word3,word4,word5)
	
	
	
