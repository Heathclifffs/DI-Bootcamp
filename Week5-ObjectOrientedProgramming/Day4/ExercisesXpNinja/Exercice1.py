# Exercise 1 : Restaurant Menu Manager - Regular Expressions
# Instructions
# Goal: The Manager wants to have a special Valentine’s night, but there are some rules.



# Create a new list of special Valentine’s day items inside the json file. For now the list should be empty.
import json
file  = "C:/Users/SHT/Desktop/Nouveau dossier/Day4/ExerciseXpGold/restaurant_menu.json"

with open(file) as f:
    data = json.load(f)
try:
    print(len(data["valentine_items"]))
except:
    data["valentine_items"] = []
 

# Ask to the manager for a new Valentine item to add, if the item is correct (ie. follows the rules below), then add it to the list inside the json file.
# Each word in the item name should begin with an uppercase letter and because it’s Valentines Day, the first word needs to begin with a capital “V”.
name = input(" Valentines Day item name: _\t")
isMeal = input(" If Valentines Day item name is a meal put (yes or no): _\t")
price = input(" Valentines Day item price: _\t")
# If the name contains connection total_words, they should begin in lowercase.
# Example: Vegetable Soup of Valentines-day
import re

def regEx():

    total_words = len(re.split("\s",name))
    x = re.findall(r"\A[V]", name)
    y= re.findall(r"\b[A-Z]",name)
    if not(x) and len(y)!=total_words:
        return False

    # The name of the meal needs to contain at least two “e”, and no numbers.
    w = re.findall("e",name)
    if isMeal.lower() != "yes" or len(w)<2:
        return False
    d = re.findall("[0-9]",name)
    if len(d)!=0:
        return False

    # The price needs to match the following pattern: XX,14, where X are numbers.
    z = re.findall("[0-9][0-9],14$",price)
    if not(z):
        return False
    return True
# Create an algorithm that displays a heart made of stars (*), when the menu is showed.

def add_valentine_item(name, price,data):
    dict = {
        "name":name,
        "price":price
    }
    data["valentine_items"].append(dict)
    return data

print(regEx)
if  regEx():
    add_valentine_item(name, price,data)
    print(data)
    with open(file,"w") as f:
        json.dump(data,f,indent = 3,sort_keys = True)
    print("Sweat heart")
else:
    print("Your item don't follow the rules of a valentine's item")
    print("Exemple : :::::::::::::::::::::\nName: Vegetable Soup of Valentines-day\nPrice: 45,14")
