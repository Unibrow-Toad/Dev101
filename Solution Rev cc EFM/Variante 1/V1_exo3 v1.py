from logging import exception
#a----------------------------
def perfect_num(n):
    if n<=0:
        raise ValueError("the number must be strictly positive!!!!")
    return sum([i for i in range(1,n) if n%i==0])==n
"""div = []
    for i in range(1,n):
        if n%i==0:
            div.append(i)
    div_sum = sum(div)
    return div_sum == n"""
while True:
    try:
        num = int(input())
        break
    except:
        continue
print(perfect_num(num))
#b----------------------------
while True:
    try:
        n = int(input())
        break
    except:
        continue
if n<6:
    print(None)
else:
    res = []
    for i in range(6,n+1):
        if perfect_num(i):
            res.append(i)
    print(res)