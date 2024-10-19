from faker import Faker
fake = Faker('en-US')
def saisir_athletes():
    num = fake.uuid4()
    nom = input("Saisir le nom de votre athlete : ")
    prenom = input("Saisir le prénom de votre athlete : ")
    nation= input("Saisir la nationalite de votre athlete : ")
    while True:
        try:
            meiltemp = float(input("Saisir le meilleur temps : "))
            break  
        except :  
            print("Erreur: Veuillez entrer un nombre valide pour le meilleur temps")
 
    return {"numero": num, "nom": nom, "prenom": prenom, "meiltemp": meiltemp, "nation": nation}


def afficher_athletes(tableau):
    if not tableau:                                         #if len(tableau)==0
        print("Aucun athletes trouvé.")
        return 
    else:
        for athletes in tableau:
            print(f"numero: {athletes['numero']}, Nom: {athletes['nom']}, Prénom: {athletes['prenom']}, meiltemp: {athletes['meiltemp']}")


def supprimer_athletes(tableau, num):
    for athletes in tableau:
        if athletes["numero"] == num:
            tableau.remove(athletes)
            print(f"L'athlete avec numero {num} a été supprimé.")
            return
    print(f"Aucun athlete trouvé avec le numero {num}.")


def ajouter_athletes(tableau):
    nouveau_athletes = saisir_athletes()
    tableau.append(nouveau_athletes)
    print("Le nouvel athlete a été ajouté.")




tableau_athletes = []

while True:
    print("\nMenu :")
    print("1. Afficher tous les athletes")
    print("2. Supprimer un athlete")
    print("3. Ajouter un athlete")
    print("4. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        afficher_athletes(tableau_athletes)
    elif choix == "2":
        meiltemp_supprimer = input("Entrez le numero du athlete à supprimer : ")
        supprimer_athletes(tableau_athletes, meiltemp_supprimer)
    elif choix == "3":
        ajouter_athletes(tableau_athletes)
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
