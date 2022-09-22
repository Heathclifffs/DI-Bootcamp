from random import *

class MyList():
	def __init__(self,l):
		self.lists=l
	def reverse(self):
		print(f'the list={self.lists}')
		self.lists.reverse()
		return self.lists
	def sort(self):
		slist=sorted(self.lists)
		return slist
	def bonus(self):
		lists2=[]
		l=len(self.lists)
		for i in range(l):
			lists2.append(randint(1,1000))
		return lists2


test=MyList(['Harold','Alpha','Omega','12','6','2001','po','full','grace','damn','something','going','wrong'])
print(f'the reversed list ={test.reverse()}')
print(f'the sorted list ={test.sort()}')
print(f'Bonus: the 2nd list with same length={test.bonus()}')
