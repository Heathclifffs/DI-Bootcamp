# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import random 

file_name = "C:/Users/SHT/Desktop/Nouveau dossier/Day4/ExerciceXP/word_list.txt"

def get_words_from_file(file):
    liste = []
    with open(file) as f:
        for line in f :
            liste.append(line[:-1])
    return liste

def get_random_sentence(length):
    liste = get_words_from_file(file_name)
    sentence = ' '.join(random.choice(liste).lower() for i in range(length))
    return sentence

# print(get_random_sentence(5))

def main():
    print('indiquer le nombre de mots que doit contenir la phrase')
    user = input("\n\tEntrer le nombre de mots (entre 2 et 20)\t")
    try:
        n = int(user)
    except:
        print("Votre saisie est incorrect")
    if (n<20 and n>2):
        print(get_random_sentence(n))


main()