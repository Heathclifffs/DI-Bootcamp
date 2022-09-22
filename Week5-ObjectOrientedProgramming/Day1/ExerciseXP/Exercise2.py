class Dog():
	def __init__(self,name,height):
		self.dog_name=name
		self.dog_height=height
	def bark(self) :
		print(f'{self.dog_name} goes woof!')
	def jump(self) :
		print(f'{self.dog_name} jumps {self.dog_height} cm high!')
def bigger():
	if sarahs_dog.dog_height > davids_dog.dog_height:
		print(f'{sarahs_dog.dog_name} is bigger')
	else:
		print(f'{davids_dog.dog_name} is bigger')

davids_dog=Dog('Rex',50)
print(f'David dog name is {davids_dog.dog_name} and height is {davids_dog.dog_height}')
davids_dog.bark()
davids_dog.jump()
sarahs_dog=Dog('Teacup',20)
print(f'Sarahs dog name is {sarahs_dog.dog_name} and height is {sarahs_dog.dog_height}')
sarahs_dog.bark()
sarahs_dog.jump()
bigger()
