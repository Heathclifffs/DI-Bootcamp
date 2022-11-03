# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.



# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.



# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)


#source  = "C:/Users/heathclifffs/DI-Bootcamp/week-ObjectOrientedProgramming/Day4/DailyChallenge/the_stranger.txt"
source  = "C:/Users/SHT/Desktop/Nouveau dossier/Day4/DailyChallenge/the_stranger.txt"

class Text():
    def __init__(self,text):
        self.text = text

    def frequency(self,word):
        seq = self.text.split(" ")
        occ = seq.count(word)
        if occ>0:
            return occ
        return None
        
    def most_common(self):
        seq = self.text.split(" ")
        # print(seq)
        common,express = 1,""
        for word in seq:
            word_occ = self.frequency(word)
            if (word_occ and word_occ > common):
                common = word_occ
                express = word
        if common == 1:
            return None
        return express,common

    def unique(self):
        seq = self.text.split(" ")
        liste = []
        for word in seq:
            word_occ = seq.count(word)
            if word_occ == 1:
                liste.append(word)
        return liste

    @classmethod
    def from_file(cls):
        with open(source) as f:
            text_instance = f.read()
        return text_instance

quote = Text(Text("").from_file())
print(quote.text)
print(quote.most_common())
print(quote.unique())
print(quote.frequency('my'))