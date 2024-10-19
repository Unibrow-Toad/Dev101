#function that calculates the product of each cubed integer below a given number
def ProduitCube(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i**3
    return prod

#asking the user for a number
while True:
    try:
        n=int(input("Enter a positive number: "))
        if n>0:
            break
    except:
        print("Please enter a valid integer")
        continue
print("The product of the cubes of the integers below",n,"is:")
print(ProduitCube(n))
#function that calculates the sum of the cubes of the first 
def summedCubes(n):
    sumProdCubes = 0
    for i in range(1,n+1):
        sumCubes += ProduitCube(i)
    return sumProdCubes

try:
    pairs=list()
    n=int(input("Enter a  number: "))
    for i in range(1,n+1):
        if n%2==0:
            pairs.append(i)
    print(pairs)
except:
    print("Please enter a valid integer")
