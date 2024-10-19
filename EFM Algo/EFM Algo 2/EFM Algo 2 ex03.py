from random import randint,choice
chambers = []
for i in range(10):
    l = {
        'num': randint(1,100),
        'beds' : randint(1,3),
        'status' : randint(0,1),
        'price' : randint(200,1000)
    }
    chambers.append(l)
#c----------------------
def chamber_sort(t):
    t.sort(key = lambda x:x['num'])
chamber_sort(chambers)
#1----------------
for chamber in chambers:
    print(chamber)
#2------------------------------------
chambers.append({'num': randint(1, 100),
                 'beds': randint(1, 3),
                 'status': randint(0, 1),
                 'price': randint(200, 1000)})
#3---------------------------------
def del_chamber():
    try:
        n = int(input("delete chamber N° : "))
        for chamber in chambers:
            if chamber['num'] == n:
                chambers.remove(chamber)
    except:
        print("invalid")
del_chamber()
#4------------------------------------
def change_status():
    try:
        n = int(input("change the status of chamber N° : "))
        for chamber in chambers:
            if chamber['num'] == n:
                chamber['status'] = abs(1 - chamber['status'])
    except:
        print("invalid")
change_status()
#5------------------------------------
with open('chambers.txt','w') as file:
    for line in chambers:
        file.write(f"{line}\n")
    print("saved successfully")
print("-"*50)
for chamber in chambers:
    print(chamber)