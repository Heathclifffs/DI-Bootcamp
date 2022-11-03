#Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"Heathclifffs",
         "payable":{ 
            "salary":10000,
            "bonus":8000
            }
        }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
data = json.loads(sampleJson)
print(data['company']['employee']['payable']['salary'])
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
data['company']['employee']['birth_date'] = "2001-06-12"
# Save the dictionary as JSON to a file.
file_name = "C:/Users/SHT/Desktop/Nouveau dossier/Day4/ExerciceXP/exercise2.json"
with open(file_name,"w") as f:
    json.dump(data,f,indent=2,sort_keys = True)
