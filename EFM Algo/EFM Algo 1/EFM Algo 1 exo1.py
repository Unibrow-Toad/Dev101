import math
while True:
    try:
        n = int(input("Entrez un nombre entier: "))
        break
    except:
        print("Veuillez entrer un nombre entier")


# Fonction pour vérifier si un nombre est premier
def isPrime(n):
    if n <= 1:
        return False   
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Check if number inferior to num are prime
print([i for i in range(n) if isPrime(i)])