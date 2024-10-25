import time,random
import json

REGIONS = ["Casablanca-Settat", "Marrakech-Safi", "Drâa-Tafilalet"]

def remplir_circonscriptions(n):
    T = []
    for i in range(n):
        nom = input(f"Nom de la circonscription {i+1} : ")
        population = int(input(f"Population de la circonscription {i+1} : "))
        date_str = input(f"Date de création (AAAA-MM-JJ) de la circonscription {i+1} : ")
        date_creation = time.strptime(date_str, "%Y-%m-%d")
        

        region = random.choice(REGIONS)

        
        est_principale = random.choice([True , False])
        
        T.append({
            "nom": nom,
            "population": population,
            "date_creation": date_creation,
            "region": region,
            "est_principale": est_principale
        })
    return T

def nombre_circonscriptions_region(T, region):
    return sum([1 for c in T if c['region'] == region])

def troisieme_plus_peuplee(T, region):
    circonscriptions_region = [c for c in T if c['region'] == region]
    if len(circonscriptions_region) < 3:
        return None
    circonscriptions_region.sort(key=lambda c: c['population'], reverse=True)
    return circonscriptions_region[2]

def region_plus_ancienne_circonscription(T):
    plus_ancienne = min(T, key=lambda c: c['date_creation'])
    return plus_ancienne['region']

def afficher_trois_plus_recentes(T):
    if len(T) < 3:
        print("Pas assez de circonscriptions.")
        return
    T.sort(key=lambda c: c['date_creation'], reverse=True)
    for c in T[:3]:
        print(f"Nom: {c['nom']}, Population: {c['population']}, Date: {time.strftime('%Y-%m-%d', c['date_creation'])}, Région: {c['region']}, Principale: {c['est_principale']}")

def supprimer_circonscription(T, nom):
    for i, c in enumerate(T):
        if c['nom'] == nom:
            if c['est_principale']:
                print(f"Impossible de supprimer la circonscription principale : {c['nom']}")
                return False
            else:
                del T[i]
                return True
    print(f"Circonscription {nom} non trouvée.")
    return False

def population_totale_region(T, region):
    return sum(c['population'] for c in T if c['region'] == region)
        #som=0 
        #for c in T:
        #    if c['region'] == region:
        #        som += c['population']

def afficher_circonscriptions_entre_dates(T, date_debut, date_fin):
    date_debut = time.strptime(date_debut, "%Y-%m-%d")
    date_fin = time.strptime(date_fin, "%Y-%m-%d")
    
    for c in T:
        if date_debut <= c['date_creation'] <= date_fin:
            print(f"Nom: {c['nom']}, Population: {c['population']}, Date: {time.strftime('%Y-%m-%d', c['date_creation'])}, Région: {c['region']}, Principale: {c['est_principale']}")

def enregistrer_region_fichier(T, region, fichier):
    circonscriptions_region = [c for c in T if c['region'] == region]
    with open(fichier, 'w') as f:
        json.dump(circonscriptions_region, f)
    print(f"Circonscriptions de la région {region} enregistrées dans {fichier}.")

def menu():
    T = []
    while True:
        print("\n1. Remplir les circonscriptions")
        print("2. Compter les circonscriptions d'une région")
        print("3. Trouver la 3e circonscription la plus peuplée")
        print("4. Trouver la région avec la plus ancienne circonscription")
        print("5. Afficher les 3 circonscriptions les plus récentes")
        print("6. Supprimer une circonscription")
        print("7. Population totale d'une région")
        print("8. Afficher les circonscriptions entre deux dates")
        print("9. Enregistrer les circonscriptions d'une région dans un fichier")
        print("10. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            n = int(input("Combien de circonscriptions souhaitez-vous ajouter ? "))
            T = remplir_circonscriptions(n)
        elif choix == '2':
            region = input(f"Entrez la région ({', '.join(REGIONS)}) : ")
            print(f"Nombre de circonscriptions dans {region} : {nombre_circonscriptions_region(T, region)}")
        elif choix == '3':
            region = input(f"Entrez la région ({', '.join(REGIONS)}) : ")
            circonscription = troisieme_plus_peuplee(T, region)
            if circonscription:
                print(f"La 3e circonscription la plus peuplée de {region} est {circonscription['nom']}, Population: {circonscription['population']}")
            else:
                print(f"Pas assez de circonscriptions dans la région {region}")
        elif choix == '4':
            region = region_plus_ancienne_circonscription(T)
            print(f"La région contenant la plus ancienne circonscription est {region}")
        elif choix == '5':
            afficher_trois_plus_recentes(T)
        elif choix == '6':
            nom = input("Entrez le nom de la circonscription à supprimer : ")
            supprimer_circonscription(T, nom)
        elif choix == '7':
            region = input(f"Entrez la région ({', '.join(REGIONS)}) : ")
            print(f"Population totale de {region} : {population_totale_region(T, region)}")
        elif choix == '8':
            date_debut = input("Entrez la date de début (AAAA-MM-JJ) : ")
            date_fin = input("Entrez la date de fin (AAAA-MM-JJ) : ")
            afficher_circonscriptions_entre_dates(T, date_debut, date_fin)
        elif choix == '9':
            region = input(f"Entrez la région ({', '.join(REGIONS)}) : ")
            fichier = input("Entrez le nom du fichier (avec extension .json) : ")
            enregistrer_region_fichier(T, region, fichier)
        elif choix == '10':
            print("Au revoir!")
            break
        else:
            print("Choix non valide, veuillez réessayer.")

menu()



#randDate(d1,d2)
#return random date between d1 et d2
#d1 = datetime.date(2020, 1, 1)
#d2 = datetime.date(2020, 12, 31)
#randDate(d1,d2) -> datetime.date(2020, 6, 15


