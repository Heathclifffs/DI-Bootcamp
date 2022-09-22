class Zoo():
	def __init__(self,zoo_name):
		self.animals=[]
		self.name=zoo_name

	
	def add_animal(self,new_animal):
		exist=0
		for e in self.animals:
			if e==new_animal:
				print(f'{new_animal} is already in the list')
				exist=1
		if exist==0:
			self.animals.append(new_animal)
			print(f'{new_animal} is add successfull')

	def get_animals(self):
		print('list of animals in zoo : ')
		for e in self.animals:
			print(e,", ",end=' ')		

		
	def sort_animals(self):
		sort=sorted(self.animals)
		dic={}
		res=[]
		x=[]
		for i in sort:
			if i[0] not in x:
				x.append(i[0])
		for i in x:
			p=[]
			for j in sort:
				if j[0]==i:
					p.append(j)
			res.append(p)
		for k,v in enumerate(res):
			dic[k]=v
		return dic

	def get_groups(self,dic):
		print(' ')
		print('list of animals by alphabet group  : ')
		print(dic)
			
ramat_gan_safari=Zoo('safari') 
print(f'welcome To Zoo  {ramat_gan_safari.name}')
num=int(input('How nany animal should we add to the zoo : '))
for i in range(num):
	add=input('Which animal should we add to the zoo : ')
	ramat_gan_safari.add_animal(add)
ramat_gan_safari.get_animals()
dic=ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups(dic)









