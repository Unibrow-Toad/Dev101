
def saisir_salarie():
    matricule = input("Saisir le matricule : ")
    nom = input("Saisir le nom : ")
    prenom = input("Saisir le prénom : ")
    while True:
        try:
            salaire = float(input("Saisir le salaire : "))
            break  
        except :  
            print("Erreur: Veuillez entrer un nombre valide pour le salaire")
    
    return {"matricule": matricule, "nom": nom, "prenom": prenom, "salaire": salaire}


def afficher_employes(tableau):
    if not tableau:                                         #if len(tableau)==0
        print("Aucun employé trouvé.")
        return 
    else:
        for employe in tableau:
            print(f"Matricule: {employe['matricule']}, Nom: {employe['nom']}, Prénom: {employe['prenom']}, Salaire: {employe['salaire']}")


def supprimer_salarie(tableau, matricule):
    for employe in tableau:
        if employe["matricule"] == matricule:
            tableau.remove(employe)
            print(f"L'employé avec matricule {matricule} a été supprimé.")
            return
    print(f"Aucun employé trouvé avec le matricule {matricule}.")


def ajouter_salarie(tableau):
    nouveau_salarie = saisir_salarie()
    tableau.append(nouveau_salarie)
    print("Le nouvel employé a été ajouté.")




tableau_employes = []

while True:
    print("\nMenu :")
    print("1. Afficher tous les employés")
    print("2. Supprimer un salarié")
    print("3. Ajouter un salarié")
    print("4. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        afficher_employes(tableau_employes)
    elif choix == "2":
        matricule_supprimer = input("Entrez le matricule du salarié à supprimer : ")
        supprimer_salarie(tableau_employes, matricule_supprimer)
    elif choix == "3":
        ajouter_salarie(tableau_employes)
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")