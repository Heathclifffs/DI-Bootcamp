from menu_manager import MenuManager
import json

def load_manager(file):
    obj = MenuManager(file)
    return obj

def show_user_menu(u_menu):
    print("\n\tUser menu\t")
    for i,item in enumerate(u_menu.menu['items']):
        print(f"{i}) {item['name']} {item['price']}")
    print("\n")
    
def add_item_to_menu(menu):
    try:
        name = input("** Item name:\t")
        price = float(input("** Item price:\t"))
        menu.add_item(name,price)
        print("item was added successfully.")
    except:
        print("Your entry is not correct")

def remove_item_from_menu(menu):
    try:
        name = input("** Item name to remove:\t")
        if (menu.remove_item(name)):
                return print("item was  deleted successfully.")
        return print("An error occurs")
    except:
        print("Something went wrong!")

def show_restaurant_menu(file):
    with open(file) as f:
        print(f.read())


file  = "C:/Users/ZONA/3D Objects/Orange DI/DI-Bootcamp/week5/Day4/ExerciseXpGold/restaurant_menu.json"
menu =load_manager(file)

while True:
    print("\t MENU ")
    print("(a) Add an item ")
    print("(d) Delete an item ")
    print("(v) View the user menu ")
    print("(m) View the restaurant menu ")
    print("(x) Exit ")
    print("-")
    choice = input("-\t").lower()

    if choice == "a":
        add_item_to_menu(menu)
    elif choice == "d":
        remove_item_from_menu(menu)
    elif choice == "v":
        show_user_menu(menu)
    elif choice == "x":
        menu.save_to_file(file,menu.menu)
        break
    elif choice == "m":
        show_restaurant_menu(file)
    else:
        print("Your choice is not correct")
