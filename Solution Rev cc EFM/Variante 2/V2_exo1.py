def VerifyPW(pwd):
    return len(str(pwd))>=8

def createCompte(nom,pwd):
    if not VerifyPW(pwd): return -1
    return {"email":nom,"password":str(pwd)}

def AfficherCompte(c):
    print(f'nom : {c.get("email")} ** mot de passe : {c.get("password")}')
#charger une liste par n comptes
comptes=list()
while True:
    nom,pwd=input("saisir nom : "),input("saisir mot de passe : ")
    c=createCompte(nom,pwd)
    if c!=-1:
        comptes.append(c)
    if(len(comptes)==4):break
#afficher la liste des comptes
for c in comptes:
    AfficherCompte(c)
        