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
