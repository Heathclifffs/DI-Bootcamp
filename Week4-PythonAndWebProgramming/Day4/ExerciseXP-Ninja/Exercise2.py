# -------------------------------------------- Exercise 2 : From English To Morse
''' Instructions
 Write a function that converts English text to morse code and another one that does the opposite.
 Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
'''
morse_table= {
    "A": ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
}

def english_to_morse(sentence):
    translation = ""
    sentence = sentence.upper()
    for e in sentence :
        if (e.isalpha()):
            translation = translation + morse_table[e]+" "
        elif (e == " "):
            translation = translation + "/"
        else :
            return False            
    return translation

def morse_to_english(expression):
    if expression == "" or expression == " ":
        return False
    expression = expression.strip()
    translation = ""
    morse = expression.split(" ")
    for ele in morse :
        isWord=0
        e = ele
        if e[0] == "/": 
            isWord = 1
            e = e[1:]       
        isFind = 0
        for k,v in morse_table.items():
            if e == v:
                isFind = 1
                if isWord == 1:
                    translation = translation + " "+k
                else:
                    translation = translation + k
        if isFind == 0:
            return False
    return translation

print(english_to_morse("It was really hard"))
print(morse_to_english(".. - /.-- .- ... /.... .- .-. -.."))

    
