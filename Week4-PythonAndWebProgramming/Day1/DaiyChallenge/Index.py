import random

thestring =str(input("Enter a string of 10 characters long:\t"))
construct = ""
if len(thestring) > 10 :
    print("string to long")
elif len(thestring) < 10:
    print("string not long enough")
else :
	print(" first character : "+thestring[0]+"\n last character :"+thestring[-1])
	print('Then, you have to construct the string character by character')
	for i in thestring : 
	    construct += i
	    print(construct)
	n=''.join(random.sample(thestring,len(thestring)))
	print("new string : "+n)
