import datetime
from math import floor
from random import randint
specific_date = datetime.date(randint(1900,2020), randint(1,12), randint(1,29))
tdy = datetime.date.today()
print(specific_date)
diff = (tdy - specific_date).days
years = floor(diff/365)
months = floor((diff%365)/(365/12))
days = floor((diff%365)%(365/12))
print(f"{days} days ,{months} months and {years} years.")
y = tdy - specific_date
x = tdy - tdy
print(y>x)


specific_date = specific_date.strftime("%d/%m/%Y")
print(specific_date)
specific_date = datetime.datetime.strptime(specific_date, "%d/%m/%Y")
print(specific_date)