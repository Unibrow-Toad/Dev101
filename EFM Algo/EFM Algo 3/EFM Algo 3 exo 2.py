#funciton that shows the multiplication table of a number given by the user
def MultiplicationTable(n):
    print(f"la table de multiplication de {n}: ")
    for i in range(0,11):print(f"{n} x {i} = {n*i}")
    print('-'*20)
#function that prints all the pair numbers below a number entered by the user
def pairNumbers():
    while True:
        try:
            n=int(input("Enter a number: "))
            break
        except:
            print("Please enter a valid integer")
    for i in range(1,n+1):
        if i%2==0:
            print(i)
    print('-'*20)
            
#ask the user for an integer
while True:
    try:
        n=int(input("Enter an number: "))
        break
    except:
        print("Please enter a valid integer")
#call the function
MultiplicationTable(n)

#show the multiplication table for numbers between 1 and 10
for i in range(1,11):
    MultiplicationTable(i)

#calling the pairNumbers function
pairNumbers()