from datetime import date,datetime

birthDate = date(2001,10,25)
currentDate = datetime.now().date()

difference = currentDate - birthDate 
#age= difference.days /365.25
years = difference.days// 365.25
nbrDays = difference.days % 365.25
nbrMonths = nbrDays // 30
nbrDaysR = nbrDays % 30


print(type(difference))
print(currentDate)
print(birthDate)
print(f"Votre âge est: {round(years)} années, {round(nbrMonths)} mois et {round(nbrDaysR)} jours")