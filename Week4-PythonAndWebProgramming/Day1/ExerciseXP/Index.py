# --------------------------------------------------- Exercise 1 : Hello World
from ast import *
print("Hello word\n"*4)

# --------------------------------------------------- Exercise 2 : Some Math
result = (99^3) * 8
print(result)

# --------------------------------------------------- Exercise 3 : What Is The Output ?
#5 < 3 #--- False
#3 == 3 #--- True
#3 == "3"#--- Error
#"3" > 3 #--- Error
#"Hello" == "hello" #---False
#---------------------------------------------------- Exercise 4 : Your Computer Brand

computer_brand = "Toshiba"
print(f"I have a {computer_brand} computer")

#----------------------------------------------------- Exercise 5 : Your Information

name = "Harold BASSOLE"
age = 21
shoe_size = 45
info = "I am {} and have {} years old. I like programation and hacking. Every time I start one of those activity i done at least my shoe size minute one it, I mean {} ".format(name,age,shoe_size)
print(info)
# ---------------------------------------------------- Exercise 6 : A & B
a =15
b=8
if a > b :
    print("Hello world")
# ---------------------------------------------------- Exercise 7 : Even or Odd
value = int(input("Enter your number"))
if value%2 == 0 :
    print("{} is odd".format(value))
else:
    print("{} is even".format(value))
# ------------------------------------------------------Exercise 8 : What’s Your Name ?
myname="Harold"
yourname=input('enter your name')
if yourname==myname:
	print('I come from futur to say you that....I am your father;see We have the same name')
else:
	print('don\'t care about me . I don\'t know who you are  ')

# ----------------------------------------------------- Exercise 9 : Tall Enough To Ride A Roller Coaster
inches =float(input("Your height in inches:\t"))
cm = inches * 2.45
if (cm > 145):
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
