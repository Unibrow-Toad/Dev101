"""

Une salle est caractérisée par son code, son libellé, nombreTables et son type. Proposer un
programme en python qui permet de :
1. Enregistrer les informations de 20 salles
2. Afficher les informations de la salle qui a le plus petit nombre de tables.
"""
from random import randint,choice
salles=[]
for i in range(1,5):
    print(f"saisir informations de la salle {i} ")
    salle=dict()
    salle["code"]=len(salles)+1 
    salle['libelle']=f'salle{salle["code"]:02d}'
    salle['nombreTables']=randint(15,24)
    salle['type']=choice(['Atelier','salle de cours','salle informatique','Amphi'])
    salles.append(salle)
print("before sort .....")
for s in salles :
    print(s)
salles.sort(key=lambda s:s.get('nombreTables'),reverse=True)

print("after sort .....")
for s in salles :
    print(s)
print(f"la salle avec le plus petit nbr de table est : \n{salles[-1]} ")
    
    