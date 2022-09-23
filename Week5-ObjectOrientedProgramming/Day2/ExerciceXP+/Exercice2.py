from Exercice1 import Family

class TheIncredibles(Family):
	def __init__(self,name):
		super().__init__(name)
		i=0
		for j in self.members:
			if i==0:
				dic={'power': 'fly','incredible_name':'MikeFly'}
				j.update(dic)
				i=i+1
			else:
				dico={'power': 'read minds','incredible_name':'SuperWoman'}
				j.update(dico)
		

	def use_power(self,name):
		v=self.is_18(name)
		if v==True:
			for i in self.members:
				for j in i.keys():
					if i[j]==name:
						print(f'{i[j]} use is power , it name is {i["power"]}')
		else:
			raise Exception(f'{name} you are not over 18 years old so you are not allowed to use your power')
	def incredible_presentation(self):
		self.family_presentation()
		print('------------------------------- Powers Description : ----------------------------')
		for i in self.members:
			print(f'***** {i["name"]} allias {i["incredible_name"]} Power can {i["power"]} *****')

		print('\n')
cooper=TheIncredibles('Coopers')
cooper.incredible_presentation()
cooper.born(name='Baby Jack ',age=0,gender='Male',is_child=True,power='Unknow Power',incredible_name='Unknow')
cooper.incredible_presentation()
'''cooper.use_power('Sarah')
cooper.use_power('Michael')
'''
