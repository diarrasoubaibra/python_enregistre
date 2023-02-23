import datetime

f = open("liste.txt", "a")
print("***************** Bienvenue sur mon site *****************")
entrer = int(input("Entrez 1 pour consulter la liste des enregistrements, ou entrez 2 pour vous enregistrer : "))
if entrer == 1:
    if f:  # Vérifier s'il y a des enregistrements dans le fichier
        print("Liste des enregistrements :")
        #for etudiant in f:
        with open("liste.txt","r") as f:
            contenu = f.read()
            print(contenu)
            f.close()
            #print(etudiant.strip())  # enlever le caractère de fin de ligne '\n' à la fin de chaque ligne
    else:
        print("Aucun enregistrement trouvé.")
elif entrer == 2:
    print("***************** Enregistrement *****************")
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    contact = input("Entrez votre contact : ")
    date = datetime.datetime.now()
    date_inscri = date.strftime("%d/%m/%y")

    # Écrire les données d'enregistrement dans le fichier
    f.write(f"Date Enregistrement : {date_inscri} - Nom : {nom}, Prénom : {prenom}, Contact : {contact}\n")

    print("Enregistrement effectué avec succès.")
else:
    print("Entrée invalide. Veuillez entrer 1 ou 2.")
