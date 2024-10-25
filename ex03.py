from random import choice
def f():
    upper_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x = []
    while upper_alphabets:
        alphabet = choice(upper_alphabets)
        x.append(alphabet)
        upper_alphabets.remove(alphabet)
    return(x)
lst = f()
print(lst)
upper_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def crypter():
    word = input()
    res = []
    for i in word.upper():
        index = upper_alphabets.index(i)
        res.append(lst[index])
    return "".join(res)
def decypter():

    word = input()
    res = []
    for i in word.upper():
        index = lst.index(i)
        res.append(upper_alphabets[index])
    return "".join(res)
print(crypter())
print(decypter())