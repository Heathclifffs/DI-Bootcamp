class pagination():
	def __init__(self,items=[],pageSize=10):
		self.pageSize=pageSize
		self.items=items
		self.page=self.pageSize
		self.totalPages=len(self.items)
		self.currentPage=1
		self.lim=0
		self.l=[]
		
	
	def getVisibleItems(self):
		print(f'# {self.items[self.l[0]:self.l[1]]}')
	
	def firstPage(self):
		self.page=self.pageSize
		self.lim=0
		self.currentPage=self.page
		self.l=[self.lim,self.page,self.currentPage]
		print('From',self.l[0],'to',self.l[1])
		return self
	
	def lastPage(self):
		a=1
		for i in self.items:
			a=self.items.index(i)
			j=a*self.pageSize
			if j >=len(self.items):
				self.page=len(self.items)
				dif=j-self.page
				self.lim=self.page-(j/a)+dif
				break
		self.currentPage=self.page
		self.l=[int(self.lim),int(self.page),int(self.currentPage)]
		print('From',self.l[0],'to',self.l[1])
		return self
	def nextPage(self,):
		print(f' The current page is {self.currentPage}')
		if self.currentPage>=self.totalPages or (self.page+self.pageSize)>=self.totalPages :
			print('the book is over ')
			return self.lastPage()
		else:
			self.lim=self.currentPage
			self.page=self.currentPage+self.pageSize
			self.currentPage=self.page
			self.l=[int(self.lim),int(self.page),int(self.currentPage)]
			print('From',self.l[0],'to',self.l[1])
			return self
		


	def prevPage(self):
		print(f' The current page is {self.currentPage}')
		if self.currentPage<=1 or (self.page-self.pageSize)< 1:
			print('the book is at is begining ')
			return self.firstPage()
		else:
			self.lim=self.currentPage-2*self.pageSize
			self.page=self.currentPage-self.pageSize
			self.currentPage=self.page
			self.l=[int(self.lim),int(self.page),int(self.currentPage)]
			print('From',self.l[1],'to',self.l[0])
			return self



	def goToPage(self,page):
		if page<1:
			print('going at begining ')
			self.currentPage=1
		elif page>len(self.items):
			print('going at end ')
			self.currentPage=len(self.items)
		else:
			print(f'going at page {page} ')
			self.currentPage=page






alphabetList = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,1,2,3,4,5,6,7".split(',')
web=pagination(alphabetList,4)
print('\n')
print('firsts Pages')
web.firstPage()
web.getVisibleItems()
print('\n')
print('next Pages')
web.nextPage()
web.getVisibleItems()
print('\n')
print('two steps next Pages')
web.nextPage().nextPage()
web.getVisibleItems()
print('\n')
print('Previous Pages')
web.prevPage()
web.getVisibleItems()
print('\n')
print('lasts Pages')
web.lastPage()
web.getVisibleItems()
print('\n')
print('two steps previous Pages')
web.prevPage().prevPage()
web.getVisibleItems()
print('\n')
web.goToPage(10)
print('next Pages')
web.nextPage()
web.getVisibleItems()
print('\n')
web.goToPage(0)
print('Previous Pages')
web.prevPage()
web.getVisibleItems()
print('\n')
web.goToPage(300)
print('next Pages')
web.nextPage()
web.getVisibleItems()










