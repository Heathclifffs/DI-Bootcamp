import random
def get_number(para):
    rd = random.randint(1,100)
    if(rd == para):
        print("Congratulation ! You got it")
    else : 
        print(f"Oops it was not {para} but {rd}")
para=int(input('you para between 1 & 100 : '))
while (para<1 or para>100):
	print ('your para must be between 1 and 100')
	para=int(input('you para between 1 & 100 : '))
get_number(para)
