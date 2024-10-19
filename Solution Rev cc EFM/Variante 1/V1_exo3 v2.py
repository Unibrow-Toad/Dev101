#number perfect 2
def number_perfect(x,nbr_perfect):
    if x>0:    
     somme_diviseur = sum ([i for i in range(1,x) if x%i==0])

     if somme_diviseur == x:return nbr_perfect.append(x)

     else: return False

nbr_perfect=[]

try :
 a=int(input("type a number : ").replace(' ',''))

 for i in range(0,a):
    number_perfect(i,nbr_perfect)
 if nbr_perfect:
    print("the perfect numbers are : {}".format(nbr_perfect)) 
 else:
    print("nothing ")
except:
   print("type a number please...")