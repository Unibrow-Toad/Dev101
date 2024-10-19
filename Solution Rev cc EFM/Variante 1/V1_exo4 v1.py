"""On souhaite écrire un programme permettant de gérer l’ensemble des salariés d’une entreprise.
Chaque salarié est connu par : un matricule, un nom, un prénom et un salaire.
a. Créer une Liste (Tableau) T et Saisir un certain nombre de salariés dans le tableau T (chaque
salarié est inséré dans le tableau comme un élément de type dictionnaire).
Il faut ensuite :
1. Afficher tous les employés de l’entreprise
2. Supprimer de l’entreprise un salarié dont le matricule est donné par l’utilisateur
3. Ajouter un nouvel salarié, dont les informations sont saisies au clavier, dans le tableau T
4. Sauvegarder les informations de tous les employés dans un fichier ‘.csv’
"""

import csv

x=0
tableau_T=[]
def tous_salarie(T,x):
   #   for i in range(x):
      matricule=input("Entrez le matricule du salarie {} : ".format(x)).replace(' ','')
      nom=input("Entrez le nom du salarie : ").replace(' ','')
      prenom=input("Entrez le prenom du salarie : ").replace(' ','')
      while True:
         try :
          salaire=float(input(("Entrez le salaire du salarie : ")).replace(' ',''))
          break
         except:
          print("error,")
      print("\n")
      tableau_T.append({
         "matricule":matricule,
         "nom":nom,
         "prenom":prenom,
         "salaire":salaire
         })

#3
def ajouter_salaries(tableau_T,x):
 while True:
   x+=1
   tous_salarie(tableau_T,x)
   if input("do you want to go out (oui ou non) :").replace(' ','').lower()=="oui":
      break
    

#1
def affichage_employes(T):
   print("Liste des salaries : \n")
   for x in tableau_T:
      print(x,"\n")


#2
def supprimer_slarie(T):
   matr=input("Entrez le matricule du slarie a supprimer : ").replace(' ','')
   for x in tableau_T:
      if x['matricule']==matr:
         tableau_T.remove(x)
         print("Salarie supprimer avec succes!") 
         return
   print("aucun salarie trouve avec ce matricule")  



#4
def sauvegarder_employes(tableau_T):
  with open('employeed.csv',mode='w',newline='')as fichier_salaries_csv:
    field_names=['matricule','nom','prenom','salaire']
    writer=csv.DictWriter(fichier_salaries_csv,field_names=field_names)
    writer.writeheader()
    for c in tableau_T:
     writer.writerow(c)
  
  print("les informations des employes ont ete sauvegardees..\n")


#finally
ajouter_salaries(tableau_T,x)

while True:
  try:
    print("\nMenu:")
    print("1. Afficher tous les employés")
    print("2. Ajouter un nouvel employé")
    print("3. Supprimer un employé")
    print("4. Sauvegarder les informations des employés dans un fichier CSV")
    print("5. Quitter")
    choix=input("Entrez votre choix : ").replace(' ','')
    if choix=='1':
       print(affichage_employes(tableau_T))
    elif choix=='2':
       ajouter_salaries(tableau_T,x)
    elif choix=='3':
       while True:
        supprimer_slarie(tableau_T)
        ask=input("voulez vous supprimer un autre salarie (oui ou non) :  ").replace(' ','')
        if ask.capitalize()=="Non":
         break
        else:
         print("Bien...\n")
    elif choix=='4':
      sauvegarder_employes(tableau_T)
    elif choix=='5':
      break
  except:
    print("error,try again...") 