class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Cat1=Cat('Harold',12)
Cat2=Cat('Ezekiel',22)
Cat3=Cat('Yipene',7)

print(f'The three Cats are : {Cat1.name} ,{Cat2.name} ,{Cat3.name}')

def oldest(age1,age2,age3):
	l=[age1,age2,age3]
	m_age=max(l)
	if m_age==Cat1.age:
		print(f'The oldest cat is {Cat1.name}, and is {Cat1.age} years old')
	elif m_age==Cat2.age:
		print(f'The oldest cat is {Cat2.name}, and is {Cat2.age} years old')
	else:	
		print(f'The oldest cat is {Cat3.name}, and is {Cat3.age} years old')

oldest(Cat1.age,Cat2.age,Cat3.age)
