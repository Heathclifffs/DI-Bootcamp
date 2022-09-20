l1=[' ',' ',' ']
l2=[' ',' ',' ']
l3=[' ',' ',' ']
print("Welcome To Tic Tac Toe")
def display_board():
	print('*********************')
	print(f'*  {l1[0]}  |  {l1[1]}  |  {l1[2]}  | *')
	print(f'* --- | --- | --- | *')
	print(f'*  {l2[0]}  |  {l2[1]}  |  {l2[2]}  | *')
	print(f'* --- | --- | --- | *')
	print(f'*  {l3[0]}  |  {l3[1]}  |  {l3[2]}  | *')
	print('*********************')

def player_input(player):
	print(f'it\'s player {player} turn :')
	row=int(input('Enter Collumn:'))
	line=int(input('Enter line:'))
	while((row<1 or row>3) or (line<1 or line>3)):
		row=int(input('row must be between 1 and 3 Enter Collumn:'))
		line=int(input('line must be between 1 and 3 Enter line:'))
	line=line-1
	row=row-1
	if line==0 and l1[row]==' ':
		l1[row]=player
	elif line==1 and l2[row]==' ':
		l2[row]=player
	elif line==2 and l3[row]==' ':
		l3[row]=player
	else :
		print("another user already is this place change it")
		player_input(player)
	




def check_win():
	if(((l1[0]==l2[0]==l3[0]) or (l1[1]==l2[1]==l3[1]) or (l1[2]==l2[2]==l3[2]) or (l1[0]==l1[1]==l1[2]) or (l2[0]==l2[1]==l2[2]) or (l3[0]==l3[1]==l3[2]))):
		if ((l1[0]==l1[1]==l1[2]==' ') or (l2[0]==l2[1]==l2[2]==' ') or (l3[0]==l3[1]==l3[2]==' ')):
			print('the Game continue')
			return False
		else:
			print('We Have A Winner')
			print(f'Comgraculation player {l1[0]} win')
			return True
	else:
		print('the Game continue')
		return False
player=['X','O']
def play():
	v=check_win()
	val=0
	while(v==False):
		display_board()
		player_input(player[val])
		if val==0:
			val=val+1
		else:
			val=val-1

		v=check_win()
	display_board()

play()







