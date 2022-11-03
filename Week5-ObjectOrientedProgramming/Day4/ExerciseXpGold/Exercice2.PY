# Exercise 2 : Giphy API #1
# Instruction
# Hint: For this exercise, check out the documentation of the Giphy API

# You will work with this part of the documention

# You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
# Explanation of the Gif URL

# q Request Paramater: Search query term or phrase. We are searching for “hilarious” gifs

# rating Request Paramater: Filters results by specified rating. We are searching for Level 1 gifs. Check out the ratings documentation

# api_key Request Paramater : GIPHY API Key. Our API KEY is hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
# Fetch the giphs from the Gif URL provided above.

# Use f-strings and variables to build the URL string we’re using for the fetch.
import json
import requests

q= 'hilarious'
rating ='g'
key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
limit = 2
url_string = f"https://api.giphy.com/v1/gifs/search?q={q}&rating={rating}&api_key={key}&limit={limit}"

response = requests.get(url_string)
print(response.status_code)


# If the status code is 200 return the result as a JSON object.
outfile = "C:/Users/SHT/Desktop/Nouveau dossier/Day4/ExerciseXpGold/outputFile.json"

if response.status_code == 200:
    data = response.json()
    with open(outfile,"w") as f1:
        json.dump(data,f1,indent = 3)   

# Only return gifs which have a height bigger then 100.



# Return the length of the object you received in the previous question.
# Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.









                     