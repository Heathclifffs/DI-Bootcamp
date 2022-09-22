class MenuManager():
	def __init__(self):
		self.dish1=['Soup',10,'B',False]
		self.dish2=['Hamburger',15,'A',True]
		self.dish3=['Salad',18,'A',False]
		self.dish4=['French Fries',5,'C',False]
		self.dish5=['Beef bourguignon',25,'B',True]
		self.dishes=[self.dish1,self.dish2,self.dish3,self.dish4,self.dish5]
		self.menu={}
		for i in range(5):
			self.menu[len(self.menu)]=self.dishes[len(self.menu)]
		print('actualy in menu : ')
		for i in self.menu:
			v=self.menu[i]
			print(v)
	
	def add_item(self,name, price, spice, gluten):
		toadd=[name,price,spice,gluten]
		self.menu[len(self.menu)]=toadd
		print('\n')
		print(f'The list after add of {name} = ')
		for i in self.menu:
			v=self.menu[i]
			print(v)

	def update_item(self,name, price, spice, gluten):
		e=0
		for i in self.menu:
			v=self.menu[i]
			if v[0]==name:
				v[1]=price
				v[2]=spice
				v[3]=gluten
				e=1
		if e==0:
			print('\n')
			print(' the dish is not in the menu')
		else:
			print('\n')
			print(f'The apudated list (update of {name} price ={price} now) =')
			for i in self.menu:
				v=self.menu[i]
				print(v)
		
	def remove_item(self,name):
		e=0
		for i in self.menu:
			v=self.menu[i]
			if v[0]==name:
				self.menu[i]=''
				#self.menu.pop(v)
				e=1
				break
		if e==0:
			print('\n')
			print(' the dish is not in the menu')
		else:
			print('\n')
			print(f'The apudated list after delete of {name} =')
			for i in self.menu:
				v=self.menu[i]
				print(v)

restaurant=MenuManager()
restaurant.add_item('Rizotto', 20,'C', True)
restaurant.update_item('Soup', 35, 'B', False)
restaurant.remove_item('Salad')
