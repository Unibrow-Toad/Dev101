while True:
    try:
        n = int(input())
        break
    except:
        continue
circonscriptions = []
for i in range(n):
    l = {
        "nom": input(),
        "population": int(input()),
        "region": input(),
        "date_creation": input(),
        "isPrincipal" : input()
    }
    if l["isPrincipal"] == "True":
        l["isPrincipal"] = True
    else:
        l["isPrincipal"] = False
    circonscriptions.append(l)
#2------
region = input()
regions = []
for element in circonscriptions:
    if element["region"] == region:
        regions.append(element["nom"])
print()
#3----------
circonscriptions_ordered = sorted(circonscriptions, key=lambda x: x['population'],reverse = True)
print(circonscriptions_ordered[2]["nom"])
#4--------------
dates = list(map(lambda x: x["date_creation"], circonscriptions))
oldest = circonscriptions[0]
for i in dates:
    year = i[:4]
    month = i[5:7]
    day = i[8:10]
    if year < oldest["date_creation"][:4]:
        oldest = circonscriptions[dates.index(i)]
    elif year == oldest["date_creation"][:4]:
        if month < oldest["date_creation"][5:7]:
            oldest = circonscriptions[dates.index(i)]
        elif month == oldest["date_creation"][5:7]:
            if day < oldest["date_creation"][8:10]:
                oldest = circonscriptions[dates.index(i)]
print(oldest["region"])
#5----------------------------------------------
most_recent = []
x = circonscriptions[0]
for j in range(3):
    for i in dates:
        year = i[:4]
        month = i[5:7]
        day = i[8:10]
        if not i in most_recent:
            if year > x["date_creation"][:4]:
                most_recent.append(circonscriptions[dates.index(i)])
                break
            elif year == x["date_creation"][:4]:
                if month > x["date_creation"][5:7]:
                    most_recent.append(circonscriptions[dates.index(i)])
                    break
                elif month == x["date_creation"][5:7]:
                    if day > x["date_creation"][8:10]:
                        most_recent.append(circonscriptions[dates.index(i)])
                        break
print(most_recent)
#6----------------------------------------------------------------
name = input()
for i in circonscriptions:
    if i["nom"] == name:
        if i["isPrincipal"]:
            circonscriptions.remove(i)
#7------------------------------------------------------
region =  input("region :")
pop_sum = 0
for i in circonscriptions:
    if i["region"] == region:
        pop_sum += i["population"]
print(pop_sum)
#8---------------------------------------------
while True:
    try:
        date1 = int(input("date1 :"))
        date2 = int(input("date1 :"))
        break
    except:
        continue
res = []
if date1>date2:
    date1,date2 = date2,date1
for i in circonscriptions:
    year = int(i["date_creation"][:4])
    if year >= date1 and year <= date2:
        res.append(i["nom"])
#9-----------------------------------
import pickle
with open("circonscriptions.dat", "wb") as f:
    pickle.dump(regions, f)
#10-----------------------------------
