# Devises
# Des Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#     #Your code starts HERE
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    #methos
    def __str__(self):
        return "{} {}".format(self.amount,self.currency)
    #method
    def __int__(self):
        return self.amount
   
    #method 
    def __repr__(self):
        return "{} {}".format(self.amount,self.currency)
    #method
    def __eq__(self,other):
        if self.currency == other.currency:
            
            return self.amount+other.amount
        else:
            return False

        
c1=Currency('dollar',5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
if c1==c3:
    print("Same")
   
else:
    print("not the same")
    
print(str(c1))
print(int(c1))
print(repr(c1))
print(int(c1)+5)
print(int(c1)+int(c2))
print(str(c1))
c1=int(c1)+5
print(str(c1))
pprint(int(c1)+int(c2))
