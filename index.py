import statistics 
noteEleve = {}
num_classe_eleves = {}

classe_eleve = str(input("entrez un nom de classe : "))
eleve = str(input ("entrez le nom de l'élève: "))
note = float(input("entrez une note :  "))
note1 = float(input("entrez une note :  "))


num_classe_eleves[eleve] = classe_eleve
noteEleve[eleve] = [note,note1]
print(noteEleve)
moyenne = statistics.mean(noteEleve[eleve])
print(moyenne)



reponse = input("voulez vous ajouter un élève ?")
while(reponse.lower() == "oui"):
    eleve_autre = (str(input ("entrez le nom de l'élève: ")))
    note1_eleve_autre =(float(input("entrez une note :  ")))
    note2_eleve_autre = (float(input("entrez une note :  ")))
    noteEleve[eleve_autre] = [note1_eleve_autre, note2_eleve_autre]

    

    #print(float(note))

    ajouterNote = input("Ajouter une note : répond Oui ou Non")
    print(repr(ajouterNote))
    if( ajouterNote.lower() == "oui"):
        note = float(input("Entrez une nouvelle note : "))
        print("Voici la note   "+ str(note))
        notesEleve = noteEleve[eleve_autre] 
        notesEleve.append(note)

        ajouterMoyenne = input("Vous voulez une  ajouter une moyenne ? ")

        if ajouterMoyenne.lower() == "oui" :
            moyenne = statistics.mean(noteEleve[eleve_autre])
            print(moyenne)

    elif ajouterNote.lower() == "non":
        print("Alors aurevoir !")

    else:
        print("Désolé veuillez refaire : ")

    reponse = input("voulez vous ajouter un élève ?")


print("au revoir")
   
#noteEleve.append(note)



