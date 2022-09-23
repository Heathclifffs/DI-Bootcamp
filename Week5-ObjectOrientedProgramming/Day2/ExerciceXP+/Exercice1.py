class Family():
	def __init__(self,name):
		self.members=[ {'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}]
		self.last_name=name
	
	def born(self,**kwargs):
		dico={}
		for arg,k in kwargs.items():
			dico[arg]=k
		self.members.append(dico)
		print(f'congratulating to the family {self.last_name} for {kwargs["name"]} born')
	
	def is_18(self,name):
		for i in self.members:
			
			for j in i.keys():
				if i[j]==name:
					if i['age']>=18:
						print(f'{name} is over 18')
						return True
					else:
						print(f'{name} is under 18')
						return False
	def family_presentation(self):
		print(f'------------------Family {self.last_name}----------------------------')
		for i in self.members: 
			print( i['name'])
		

'''cooper=Family('Cooper')
cooper.born(name='sheldon',age=0,gender='Male',is_child=True)
cooper.born(name='Penny',age=0,gender='Male',is_child=True)
cooper.is_18('Penny')
cooper.is_18('Sarah')
cooper.is_18('sheldon')
cooper.is_18('Michael')
cooper.family_presentation()
'''
