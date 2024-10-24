def isPalendrome(n):
    return str(n) == str(n)[::-1]
while True:
    try:
        n = int(input())
        if isPalendrome(n):
            break
    except:
        continue