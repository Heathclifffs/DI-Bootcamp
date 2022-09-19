
# ------------------------------------------------- Exercise 1 : Convert Lists Into Dictionarie
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {}
for i,j in zip(keys,values):
    dict[i]=j
print(dict)

'''
# ------------------------------------------------- Exercise 2 : Cinemax
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost = 0
for k,v in family.items():
	if v<3:
		print(f"{k} have to pay 0$")
	elif(v>3 and v<12):
		cost += 10
		print(f"{k} have to pay 10$")
	else:
		cost += 15
		print(f"{k} have to pay 15$")
		print(f"Family total cost : {cost}")
		name = input("your name : ")
		age = int(input("your age : "))
	if name not in family.keys():
		family[name] = age
	print(family)

'''
# ------------------------------------------------Exercise 3: Zara

brand = {
    "name": "Zara" ,
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona ",
    "type_of_clothes": ["men", "women", "children", "home"] ,
    "international_competitors": ["Gap", "H&M", "Benetton"] ,
    "number_stores": 7000 ,
    "major_color": 
    {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
name = brand["name"]
print(f"{name} clients are : ")
for i in brand["type_of_clothes"]:
    print(i)
brand.update({"country_creation":"Spain"})
if 'international_competitors' in brand.keys():
    brand["number_stores"] += 1
#  Delete date of creation
del brand["creation_date"]
# print(brand)
# Print the last international competitor.
print(brand["international_competitors"][-1])
# Print the major clothes colors in the US.
major_color = brand["major_color"]
print(major_color["US"])
# length of the dictionary
print(len(brand.items()))
# the keys of the dictionary
print(brand.keys())
#  Create another dictionary called more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
# add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(len(brand.items()))
# the value of the key number_stores.
print(brand["number_stores"])


#  ----------------------------------------------------------------------- Exercise 4 : Disney Characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# for loop to recreate the 1st result
values = list(range(len(users)))
disney_users_A = {}
for i,j in zip(users,values):
    disney_users_A.update({i:j})
print(disney_users_A)
# Use a for loop to recreate the 2nd result
disney_users_B = {}
for i,j in zip(users,values):
    disney_users_B.update({j:i})
print(disney_users_B)
# a method to recreate the 3rd result
users = sorted(users)
disney_users_C = {}
for i,j in zip(users,values):
    disney_users_C.update({i:j})
print(disney_users_C)
# recreate the 1st result for : 
# 1 characters, which names contain the letter “i”.
disney_users_I = {}
for i,j in zip(users,values):
    if "i" in i:
        disney_users_I.update({i:j})
print(disney_users_I)
# The characters, which names start with the letter “m” or “p”
disney_users_M_P = {}
for i,j in zip(users,values):
    if "M" == i[0] or "P" == i[0]:
        disney_users_M_P.update({i:j})
print(disney_users_M_P)
