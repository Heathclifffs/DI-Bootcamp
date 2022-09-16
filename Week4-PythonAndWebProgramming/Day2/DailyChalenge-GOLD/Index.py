'''
	Instructions
Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake as seen below:
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

Bonus : If they were born on a leap year, display two cakes !

'''
age=input('enter your birthdate : DD/MM/YYYY :')
print('your birthdate = ',age)
age=age[6:len(age)]
print('your year of born is = ',age)
y=int(age)
age=2022 - int(age)
print('your age is = ',age)
age=str(age)[-1]
age=int(age)
val=int((13-age)/2)
print(val)
print('the number of  candles = ',age)
for i in range(3):
	print(' ',end='')
for i in range(val):
	print('-',end='')
for i in range(age):
	print('i',end='')
for i in range(val):
	print('-',end='')
for i in range(3):
	print(' ',end='')
print(' ')
for i in range(3):
	print(' ',end='')
print('|:H:a:p:p:y:|')
for i in range(2):
	print(' ',end='')
for i in range(1):
	print(' ',end='')
print('|           |')
for i in range(0):
	print(' ',end='')
for i in range(19):
	print("-",end='')
print('')
print('|^^^^^^^^^^^^^^^^^|')
print('|:B:i:r:t:h:d:a:y:|')
print('|                 |')
print('|                 |')
print('~~~~~~~~~~~~~~~~~~~')

#Bonus
lis=[1900,1904,1908,1912,1916,1920,1924,1928,2020,2024,2028,2032,2036.,2040,2044,2048,2100,2104,2108,2112,2116,2120,2124,2128]
if y in lis:
	for i in range(3):
		print(' ',end='')
	for i in range(val):
		print('-',end='')
	for i in range(age):
		print('i',end='')
	for i in range(val):
		print('-',end='')
	for i in range(3):
		print(' ',end='')
	print(' ')
	for i in range(3):
		print(' ',end='')
	print('|:H:a:p:p:y:|')
	for i in range(2):
		print(' ',end='')
	for i in range(1):
		print(' ',end='')
	print('|           |')
	for i in range(0):
		print(' ',end='')
	for i in range(19):
		print("-",end='')
	print('')
	print('|^^^^^^^^^^^^^^^^^|')
	print('|:B:i:r:t:h:d:a:y:|')
	print('|                 |')
	print('|                 |')
	print('~~~~~~~~~~~~~~~~~~~')
	print('\n your born year is a leap year')
	












