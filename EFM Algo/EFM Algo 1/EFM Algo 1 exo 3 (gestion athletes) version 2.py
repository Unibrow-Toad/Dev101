from random import randint,choice
athletes = []
while True:
    try:
        x = int(input())
        break
    except:
        continue
for i in range(x):
    l = { 'num' : randint(1,100),
        "f_name": choice(["f_name A", "f_name B", "f_name C", "f_name D", "f_name E", "f_name F", "f_name G", "f_name H", "f_name I",
         "f_name J", "f_name K", "f_name L", "f_name M"]),
        "l_name": choice(["l_name A", "l_name B", "l_name C", "l_name D", "l_name E", "l_name F", "l_name G", "l_name H", "l_name I",
         "l_name J", "l_name K", "l_name L", "l_name M"]),
        'nation': choice(["Australia","Brazil","Canada","China","Egypt","France","Germany","India","Japan","Mexico","Nigeria","Russia","South Africa","Spain","United Kingdom","United States"]),
        'best_time': randint(60,180)
    }
    athletes.append(l)
for athlete in athletes:
    print(athlete)
#c-----------------
athletes.sort(key=lambda x:x['num'])
print("----------------------")
for athlete in athletes:
    print(athlete)
#2----------------
try:
    n = int(input())
    for athlete in athletes:
        if n == athlete['num']:
            athletes.remove(athlete)
except:
    print("invalid input")
print("----------------------")
for athlete in athletes:
    print(athlete)
#3------------------
l = { 'num' : randint(1,100),
        "f_name": choice(["f_name A", "f_name B", "f_name C", "f_name D", "f_name E", "f_name F", "f_name G", "f_name H", "f_name I",
         "f_name J", "f_name K", "f_name L", "f_name M"]),
        "l_name": choice(["l_name A", "l_name B", "l_name C", "l_name D", "l_name E", "l_name F", "l_name G", "l_name H", "l_name I",
         "l_name J", "l_name K", "l_name L", "l_name M"]),
        'nation': choice(["Australia","Brazil","Canada","China","Egypt","France","Germany","India","Japan","Mexico","Nigeria","Russia","South Africa","Spain","United Kingdom","United States"]),
        'best_time': randint(60,180)
    }
athletes.append(l)
print("----------------------")
for athlete in athletes:
    print(athlete)

#4-----------------
try:
    num = int(input("enter a number : "))
    for athlete in athletes:
        if num == athlete['num']:
            try:
                athlete['best_time'] = int(input(""))
            except:
                "invalid"
except:
    print("invalid")
print("----------------------")
for athlete in athletes:
    print(athlete)
#5-------------------

with open('athletes.txt','w') as file:
    for line in athletes:
        file.write(f"{line}\n")
print("saved successfully!!!")
