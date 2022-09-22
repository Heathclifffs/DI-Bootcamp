class circle():
	def __init__(self):
		self.radius=10
		
	
	def perimeter(self):
		Perimeter=2*3.14*self.radius
		print(f'perimeter={Perimeter}')
	def area(self):
		Area=3.14*self.radius*self.radius
		print(f'Area={Area}')

		return Area
	def geometric(self):
		print(f'radius={self.radius}')
		
geo=circle()
geo.geometric()
geo.perimeter()
geo.area()
