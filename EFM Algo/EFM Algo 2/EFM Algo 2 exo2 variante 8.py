#exercice2.2 variante:8

def produitcarre(n):
    p=1 
    for x in range(1,n+1):
        p*=x 
    return p 
    
while True:
    try:
        N=int(input("type a number : ").strip())
        S=0
        for i in range(1,N+1):
            S+=1/produitcarre(i)
        print(S)
        break
    except:
        print("you must type a number")


#exercice2.3 variante : 8 

list=[]

def nbr_pairs(n,list):
    for x in range(1,n+1):
        if x%2==0:
            list.append(x)
            
while True:
    n=input("type a number : ").strip()
    if n.isdigit():
        n=int(n)
        break
nbr_pairs(n,list)
print(list)
