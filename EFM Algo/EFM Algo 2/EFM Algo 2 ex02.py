from random import randint
#1-----------------------
t = [randint(1,5) for x in range(10)]
res = [x for x in t if t.count(x)<3]
print(t)
print(res)
t = list(filter(lambda x:t.count(x)<3,t))
print(t)
#2---------------------
def prime_num(n):
    primes = []
    for i in range(1, n + 1):
        divs = 0
        for j in range(1,i+1):
            if i%j==0:
                divs += 1
        if divs == 2:
            primes.append(i)
    return primes
try:
    n = int(input())
    print(prime_num(n))
except:
    print("invalid")