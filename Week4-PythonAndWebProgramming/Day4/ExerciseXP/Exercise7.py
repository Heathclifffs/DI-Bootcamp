
# ---------------------------------------------------------------- Exercise 7 : Temperature Advice
''' Instructions
 1.Create a function called get_random_temp()
	.This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
 	. Test your function to make sure it generates expected results.
 2.Create a function called main().
	.Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
	.Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.” 
 3.Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
	.below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
	.between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
	.between 16 and 23
	.between 24 and 32
	.between 32 and 40
 4.Change the get_random_temp() function:
	.Add a parameter to the function, named ‘season’.
	.Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
 Now that we’ve changed get_random_temp(), let’s change the main() function:
	.Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
	.Use the season as an argument when calling get_random_temp().

'''
import random
def get_random_temp():
    return random.randrange(-10,40)
test = [get_random_temp() for ele in range(10)]
print(test)
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if(temp < 0):
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif (temp>0 or temp<=16):
        print("Quite chilly! Don’t forget your coat")
    elif (temp>16 or temp<=23):
        print("Relatively nice")
    elif (temp>24 or temp<=32):
        print("Litle bit hot")
    else:
        print("Very hot")

main()
def get_random_temp(season):
    if season == "winter":
        return random.randrange(-10,16)
    if season == "automn" or season == "fall":
        return random.randrange(16,23)
    if season == "summer":
        return random.randrange(24,32)
    if season == "spring":
        return random.randrange(33,40)
    else:
        return random.randrange(-10,40)
def main():
    season = input("Enter for a season : ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if(temp < 0):
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif (temp>0 or temp<=16):
        print("Quite chilly! Don’t forget your coat")
    elif (temp>16 or temp<=23):
        print("Relatively nice")
    elif (temp>24 or temp<=32):
        print("Litle bit hot")
    else:
        print("Very hot")
main()
