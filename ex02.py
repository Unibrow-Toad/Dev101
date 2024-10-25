def perfect(n):
    somme = 0
    for i in range(1, n):
        if n % i == 0:
            somme += i
    if somme == n:
        return True
    else:
        return False
try:
    n = int(input())
    if n>0:
        if perfect(n):
            print("perfect :)")
        else:
            print("not perfect :(")
except:
    print("invalid input")