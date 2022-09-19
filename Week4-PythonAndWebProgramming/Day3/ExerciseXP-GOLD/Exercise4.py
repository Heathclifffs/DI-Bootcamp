# ------------------------------------------------------ Fruit Shop
''' Instructions

 items = {
     "banana": 4,
     "apple": 2,
     "orange": 1.5,
     "pear": 3
 }

     Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
     Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
     write some code to calculate how much it would cost to buy everything in stock.

 items = {
     "banana": {"price": 4 , "stock":10},
     "apple": {"price": 2, "stock":5},
     "orange": {"price": 1.5 , "stock":24},
     "pear": {"price": 3 , "stock":1}
 }
'''
item = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for cle,valeur in item.items():
    print(cle,"prix-->",valeur)
somme=0
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
    }
for cle,valeur in items.items():
    somme+=items[cle]['price']*items[cle]['stock']
print("Prix total:",somme)
    
