# -------------------------------------------------------- Add Your Own Birthday
''' Instructions

     Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
         Ask the user for a person’s name – store it in a variable.
         Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
         Now add this new data into your dictionary.
     Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.
'''
birthdays={'armin':'1960/12/24',
           'mikassa':'2009/02/05',
           'reiner':'1994/03/29',
           'eren':'2003/07/16',
           'zecke':'2001/06/2001'}
name=input("Entrer your name:")
birth=input("Entrer your Birthdate yyy/mm/dd:")
#birthdays[name]=birth
t=0
for cle in birthdays.keys():
    if name==cle:
        print(f"{name} is found and The corresponding birthday is found:",birthdays[name])
        t=1
        break
if t==0:
	print(f"we add {name} to the list with birthday date {birth}")
	birthdays[name]=birth
	print(birthdays)
