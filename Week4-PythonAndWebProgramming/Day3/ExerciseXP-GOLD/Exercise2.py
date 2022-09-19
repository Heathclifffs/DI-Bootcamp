# -------------------------------------- Birthdays Advanced
''' Instructions

     Before asking the user to input a person’s name print out all of the names in the dictionary.
     If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)
'''

birthdays={'armin':'1960/12/24',
           'mikassa':'2009/02/05',
           'reiner':'1994/03/29',
           'eren':'2003/07/16',
           'zecke':'2001/06/2001'}
print("All bithday:",birthdays)
t=0
name=input("Enter a name:")
for cle in birthdays.keys():
    if name==cle:
        t=1
        print("The birthday of ",cle)
        print(birthdays[name])
if t==0:
 print("Sorry, we don't have the birthday information for",name)

        
