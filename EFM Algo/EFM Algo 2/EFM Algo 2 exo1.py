from random import randint
#ask user for a number
while True:
    try:
        N=int(input("Enter a number: "))
        break
    except:
        print("Veuillez entrer un nombre entier")
        continue
#generate a list of random numbers with length N
T=[randint(0,20) for i in range(N)]
print(T)
#ask user for a number
while True:
    try:
        a=int(input("Enter a number: "))
        break
    except:
        print("Veuillez entrer un nombre entier")
        continue
#delete all instances of a from the list if a is repeated at least 3 times
if T.count(a)>=3:
    T = [x for x in T if x != a]
print(T)
