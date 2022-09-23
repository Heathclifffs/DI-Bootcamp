class Dog():
	def __init__(self,name, age, weight):
		self.name=name
		self.age=age
		self.weight=weight
	
	def bark (self):
		s=self.name+' is barking'
		return s
	
	def speed_run(self):
		speed=((self.weight/self.age)*10)
		return speed

	def fight(self,other_dog):
		weight1=self.speed_run()*self.weight
		weight2=other_dog.speed_run()*other_dog.weight
		if weight1>weight2:
			print(self.name,f' power= {weight1} is winner of the fight vs ',other_dog.name,f' power= {weight2}')
		elif(weight1==weight2):
			print(f'tie in fight {self.name} and {other_dog.name} are equal')
		else:
			print(f'{other_dog.name} power= {weight2} is the winner of the fight vs {self.name} power= {weight1}')

harry=Dog('harry',12,13)
ron=Dog('ron',22,20)
hermione=Dog('hermione',14,25)
'''
print(harry.bark())
print(harry.name,' speed = ',harry.speed_run())
print(hermione.bark())
print(hermione.name,' speed = ',hermione.speed_run())
print(ron.bark())
print(ron.name,' speed = ',ron.speed_run())
harry.fight(ron)
harry.fight(hermione)
harry.fight(harry)
ron.fight(hermione)
'''








