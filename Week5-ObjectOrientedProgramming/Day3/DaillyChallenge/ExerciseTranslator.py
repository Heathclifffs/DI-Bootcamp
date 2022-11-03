''' Instructions :Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
Look at this result :
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
You have to recreate the result using a translator module.
from translate import Translator
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translator=Translator(from="fr",to_lang="zh")
translator=Translator()
translation=translator.translate("bonjour")
 print(translation)

# from translate import Translator
# translator= Translator(to_lang="nl")
# translation = translator.translate("je")
# print(translation)'''

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
english=dict()
from deep_translator import GoogleTranslator
for i in range(len(french_words)):
    
    text=french_words[i]
    traduction=GoogleTranslator(source="fr" ,target="en").translate(text)
    english[text]=traduction
print(english)