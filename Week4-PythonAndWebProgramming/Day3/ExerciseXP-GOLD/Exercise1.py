#  ------------------------------------------------------- Birthday Look-up
''' Instructions

     Create a variable called birthdays. Its value should be a dictionary.
     Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
     Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
         Ask the user to give you a person’s name and store the answer in a variable.
         Get the birthday of the name provided by the user.
         Print out the birthday with a nicely-formatted message.
'''
birthday={'armin':'1960/12/24',
           'mikassa':'2009/02/05',
           'reiner':'1994/03/29',
           'eren':'2003/07/16',
           'zecke':'2001/06/2001'}
print("Welcome, you can see the birthdays of the people in the list below")
print(birthday)
t=0
yname=input("Enter un name:")
for cle in birthday.keys():
    if yname==cle:
        t=1
        print("The birthday of ",cle)
        print(birthday[yname])
if t==0:
	print("This name is not in our dictionary")
