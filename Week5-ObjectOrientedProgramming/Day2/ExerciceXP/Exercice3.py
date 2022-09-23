from Exercice2 import Dog
from random import randint
class PetDog(Dog):
	def __init__(self,name,age,weight):
		super().__init__(name,age,weight)
		self.trained=False

	def train(self):
		self.trained=True
		print(self.bark())
	
	def play(self,*args):
		print(f'{args} all play together')

	def do_a_trick(self):
		if self.trained==True:
			l=[self.name+' does a barrel roll', self.name+' stands on his back legs', self.name+' shakes your hand', self.name+' plays dead']
			val=randint(0,3)
			print(l[val])
		else:
			print(f'{self.name} is not trained ')

harry=PetDog('harry',12,13)
ron=PetDog('ron',22,20)
hermione=PetDog('hermione',14,25)

harry.train()
ron.train()
#hermione.train()
harry.fight(hermione)
harry.play(harry.name,ron.name,hermione.name)
harry.do_a_trick()
hermione.do_a_trick()
ron.do_a_trick()
