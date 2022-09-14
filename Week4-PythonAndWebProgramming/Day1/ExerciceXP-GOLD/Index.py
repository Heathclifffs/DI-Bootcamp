# ------------------------------------------------------------------- Exercise 1 : Hello World-I Love Python
print("Hello world\n" * 4 +"I love python\n" * 4)

# ------------------------------------------------------------------- Exercise 2 : What Is The Season ?

month = int(input("what is  month (1 to 12). ?"))
if month in [12,1,2] : 
    print("It is :\tWinter")                      
elif month in [9,10,11] :
    print("It is :\tAutumn")                      
elif month in [6,7,8] :
    print("It is :\tSummer")                      
elif month in [3,4,5] :
    print("It is :\tSpring")       
else : 
    print("read instruction, the mouth should be between 1 and 12")


