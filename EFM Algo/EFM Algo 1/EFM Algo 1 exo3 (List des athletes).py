from random import randint,uniform
from faker import Faker
fake = Faker('en-US')
#Athlete = {'num':num, 'prenom':prenom, 'Nom':nom, 'Nation':nation, 'MeiTemp':MeiTemp}
#a list of athletes
Athletes = []

#function for adding athletes to the list
def AddAthlete():
    #ask user for the number of athletes to add
    try:
        n=int(input('Entrez le nombres d''athletes: '))
    except:
        print("Please enter a valid integer")
    for i in range(1,n+1):
        Athlete = {}
        Athlete['num'] = randint(1,100)
        Athlete['prenom'] = fake.first_name()
        Athlete['Nom'] = fake.last_name()
        Athlete['Nation'] = fake.country()
        Athlete['MeiTemp'] = uniform(5,10)
        Athletes.append(Athlete)
#function for printing athletes
def DisplayAll(Athletes):
    if len(Athletes) == 0:
        print("There are no athletes",'-'*50,sep="\n")  
        return 
    for row in Athletes:
        print(f"{row['num']} {row['prenom']} {row['Nom']} {row['Nation']} {row['MeiTemp']:.2f}",sep="\t")
    print ('-'*50)    

#function for sorting athletes by number in ascending order
def SortByNum(Athletes):
    Athletes = sorted(Athletes, key=lambda x: x['num'])
    DisplayAll(Athletes)

#function to delete an athlete by number
def DeleteAthlete(Athletes):
    try:
        n=int(input('Entrez le numéro de l''athlète que vous voulez supprimer: '))
    except:
        print("Please enter a valid integer")
    #check if the athlete exists
    if n not in [row['num'] for row in Athletes]:
        print('L''athlète n''existe pas')
        return
    #remove the athlete from the list
    for row in Athletes:
        if row['num'] == n:
            Athletes.remove(row)

#function to add an athlete manually
def AddAthleteManually():
    Athlete = {}
    while True:
        try:
            Athlete['num'] = input(input('Enter the athlete\'s number: '))
            break
        except:
            print("Please enter a valid integer")
    Athlete['prenom'] = input('Enter the athlete\'s first name: ')
    Athlete['Nom'] = input('Enter the athlete\'s last name: ')
    Athlete['Nation'] = input('Enter the athlete\'s country: ')
    while True:
        try:
            Athlete['MeiTemp'] = float(input('Enter the athlete\'s best time:  '))
            break
        except:
            print("Please enter a valid float")
    Athletes.append(Athlete)
    SortByNum(Athletes)

#function to change athlete's best time by athlete number
def ChangeBestTimeByNum(Athletes):
    while True:
        try:
            n=int(input('Entrez le numéro de l''athlète: '))
            break
        except:
            print("Please enter a valid integer")
    if n not in [row['num'] for row in Athletes]:
        print('L''athlète n''existe pas')
        return
    for row in Athletes:
        if row['num'] == n:
            while True:
                try:
                    row['MeiTemp'] = float(input('Enter the new best time:  ')) 
                    print('Best time changed successfully')
                    break
                except:
                    print("Please enter a valid float")

#function to save athletes to a text file
def SaveToTextFile(Athletes):
    with open('Athletes.txt','w') as file:
        for row in Athletes:
            file.write(f"{row['num']} {row['prenom']} {row['Nom']} {row['Nation']} {row['MeiTemp']:.2f}\n")




#----------------------------------------------------------------------------------------------------------

#---------------------------------------------------Menu---------------------------------------------------
while True:
    print("A. Add  random Athletes")
    print("S. sort Athletes by number in ascending order")
    print("1. Display all athletes")
    print("2. Delete an Athlete by number")
    print("3. Add an athlete manually")
    print("4. Change best time of an athlete")
    print("5. Save athletes to a text file")
    print('6. Exit')
    choice = input("Enter your choice: ")
    if choice.lower() == 'a':
        AddAthlete()
    elif choice.lower() == 's':
        SortByNum(Athletes)
    elif choice.lower() == '1':
        DisplayAll(Athletes)
    elif choice.lower() == '2':
        DeleteAthlete(Athletes)
    elif choice.lower() == '3':
        AddAthleteManually()
    elif choice.lower() == '4':
        ChangeBestTimeByNum(Athletes)
    elif choice.lower() == '5':
        SaveToTextFile(Athletes)
    elif choice.lower() == '6':
        break
    else:
        print("Invalid choice. Please try again.")
