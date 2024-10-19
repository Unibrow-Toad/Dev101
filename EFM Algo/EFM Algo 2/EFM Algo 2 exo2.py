#a fucntion that calculates product of each integer till a given number
def Produit(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod
#function that calculates the sum of fractions of products of consecutive integers
def Somme(n):
    somme=0
    for i in range(1,n+1):
        somme+=1/Produit(i)
    return somme
#asking the user for a number
while True:
    try:
        n=int(input("Enter a positive number: "))
        if n>0:
            break
    except:
        print("Please enter a valid integer")
        continue
#printing the product of the integers
print("The product of the integers till",n,"is:")
print(Produit(n))
#printing the sum of the fractions
print("The sum of the fractions of the products of the integers till",n,"is:")
print(Somme(n))

#a list that coontains all pair numbers below n
pairs=list()
for i in range(1,n+1):
    if i%2==0:
        pairs.append(i)
print(pairs)

