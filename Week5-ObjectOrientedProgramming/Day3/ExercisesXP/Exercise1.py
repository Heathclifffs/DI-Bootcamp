# ----------------------------------------- Exercice 1 : Functions

# abs(), int(), input().
import math
def absolute(n):
    return abs(n)

print(absolute.__doc__)
print("")
number=int(input("Entrer un nombre:"))
value=absolute(number)
print("Valeur absolue :",value)
