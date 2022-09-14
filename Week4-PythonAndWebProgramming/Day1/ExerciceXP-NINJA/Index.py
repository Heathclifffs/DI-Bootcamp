# ------------------------------------------------- Exercise 1 : Use The Terminal
#i can call python3 if i am not in the executable directory cause python is in the path as environement variable and those variable can be call every where through a command  .

# ------------------------------------------------- Exercise 2 : Alias
#using linux : alias py="python3" after we just have to do py {myProgramName.py}

#-------------------------------------------------- Exercise 3 : Outputs
# 3 <= 3 < 9  #True
# 3 == 3 == 3 #True
# bool(0) #False
# bool(5 == "5") #False
# bool(4 == 4) == bool("4" == "4") #True
# bool(bool(None)) #False
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x) #x is True
print("y is", y) #y is False
print("a:", a)   #a: 5
print("b:", b)   #b: 10

#---------------------------------------------------- How Many Characters In A Sentence ?
my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
len(my_text)
print(len(my_text))

#------------------------------------------------------Longest Word Without A Specific
i=1
while(i==1):
	long_sentence = ""
	record = 0
	iswith = True
	l_r = len(record)
	l_s = len(long_sentence)
	while l_r > l_s or iswith == True:
			record=record+1
  	  print(f"\n Higher score :record")
  	  long_sentence = input('long sentence without a "A"')
  	  if "A".lower() in long_sentence.lower():
  	      iswith = True
  	      print(f"There is a A : {l_s}")
  	  else:
  	      iswith = False
  	      l_s= len(long_sentence)
  	      print(f"You got : {l_s}")
