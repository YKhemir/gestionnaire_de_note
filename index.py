# num_classe_eleves  un fichier json et en lien avec noteEleve 
import statistics 
noteEleve = {}

classe_eleve = str(input("entrez un nom de classe : "))
eleve = str(input ("entrez le nom de l'élève: "))
note = float(input("entrez une note :  "))
note1 = float(input("entrez une note :  "))

# noteEleve = {
#          "jojo" : {"classe": "3ème 5", "notes": [10, 10]}
#              }

noteEleve[eleve] = {"classe": classe_eleve, "notes": [note, note1]} 
print(noteEleve)
moyenne = statistics.mean(noteEleve[eleve]["notes"])
print("La moyennes est de " + str(moyenne))



reponse = input("voulez vous ajouter un élève ? ")
while(reponse.lower() == "oui"):
     classe_eleve_autre = str((input("entrez un nom de classe : ")))
     eleve_autre = (str(input ("entrez le nom de l'élève: ")))
     note1_eleve_autre =(float(input("entrez une note :  ")))
     note2_eleve_autre = (float(input("entrez une note :  ")))

     noteEleve[eleve_autre] = { "classe": classe_eleve_autre ,
                                "notes": [note1_eleve_autre, 
                                          note2_eleve_autre]
                              }
     moyenne_autre = statistics.mean(noteEleve[eleve_autre]["notes"])
     print(f"La moyenne est de {moyenne_autre}")

    

    

     ajouterNote = input("Ajouter une note : répond Oui ou Non")

     if( ajouterNote.lower() == "oui"):
         note = float(input("Entrez une nouvelle note : "))
         print("Voici la note   "+ str(note))
         #notesEleve = { "classe": classe_eleve_autre ,
          #              "notes" : [note1_eleve_autre, note2_eleve_autre]} 
         #notesEleve["notes"].append(note)
         notesEleve = noteEleve[eleve_autre]["notes"]
         notesEleve.append(note)
         ajouterMoyenne = input("Vous voulez afficher sa  moyenne ? ")

         if ajouterMoyenne.lower() == "oui" :
             moyenne = statistics.mean(noteEleve[eleve_autre]["notes"])
             print(moyenne)

     elif ajouterNote.lower() == "non":
         print("Alors aurevoir !")

     else:
         print("Désolé veuillez refaire : ")

     reponse = input("voulez vous ajouter un élève ?")






