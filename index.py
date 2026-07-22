import statistics 
noteEleve = {}
eleve = str(input ("entrez le nom de l'élève: "))
note = float(input("entrez une note :  "))
note1 = float(input("entrez une note :  "))


noteEleve[eleve] = [note,note1]
print(noteEleve)
moyenne = statistics.mean(noteEleve[eleve])
print(moyenne)

resultat = print("salut")
print(resultat)

reponse = input("voulez vous ajouter un élève ?")
while(reponse == "oui"):
    print(str(input ("entrez le nom de l'élève: ")))
    print(float(input("entrez une note :  ")))
    print(float(input("entrez une note :  ")))
    moyenne = statistics.mean(noteEleve[eleve])
    print(moyenne)

# noteEleve = {}
# noteEleve["Yasmine"] = 15
# noteEleve["Yasmine"] = 12
# print(noteEleve)



# print(float(note))
#ajouterNote = input("Ajouter une note : répond Oui ou Non")
# if( ajouterNote == "Oui"):
#     print("Voici la note   "+ note)
# elif ajouterNote != "Non" and ajouterNote != "Oui":
#     print(note)
# else:
#     print("Désolé veuillez refaire : ")

#noteEleve.append(note)

# test = {"yasmine":[12,15,18]}
# test["yasmine"].append(10)

# print(test)

