with open("test.txt", "w") as fichier:
    fichier.write("Bonjour") # fichier étiquette temporaire 

# lire 
with open("test.txt", "r") as fichier:
    print(fichier.read())

# fichier json (stock les dictionnnaire )
import json

dico = { "nom": "jojo", "age" : 13, "paypay" : "cartoon"}

with open("test.json", "w") as fichier_json: # ouvrir le fichier
    json.dump(dico, fichier_json)   # mettre dedans le dico 

# charger un fichier json 
with open("test.json", "r") as fichier_json:
     content_json = json.load(fichier_json)
     print(content_json)