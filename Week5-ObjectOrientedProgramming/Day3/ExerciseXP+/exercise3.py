'''string Module
Instructions
Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
Hint: use the string module'''
import random
import string

def chaine(length):
    str= string.ascii_letters
    return ''.join(random.choice(str) for i in range(length))
print("La chaine est :",chaine(5))
        