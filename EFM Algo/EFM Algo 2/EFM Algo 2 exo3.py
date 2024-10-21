#--------------------------------------------Modules--------------------------------------------
import random
#--------------------------------------------Functions--------------------------------------------
#function for adding a number of rooms to the list
def AddRooms(Chambres):
    #new code
    while True:
        try:
            n = int(input("Enter number of rooms to add: ") or 0)
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer")
    Chambres.extend(sorted([{'num': random.randint(1, 100), 'numOfBeds': random.randint(1, 4), 'freeOrBooked': random.choice(['free', 'booked']), 'price': round(random.uniform(100, 500),2)} for i in range(n)], key=lambda x: x['num']))
    #old code
    '''while True:
        try:
            n = int(input("Enter number of rooms to add: "))
            break
        except ValueError:
            print("Please enter a valid integer")

    for i in range(n):
        Chambre = {'num': random.randint(1, 100), 'numOfBeds': random.randint(1, 4), 'freeOrBooked': random.choice(['free', 'booked']), 'price': random.uniform(100, 500)}
        Chambres.append(Chambre)
        Chambres.sort(key=lambda x: x['num'])
'''
#function for displaying all the rooms
def DisplayAll(Chambres):
#new code
    print('-' * 50);print("\n".join([f"{row['num']} {row['numOfBeds']} {row['freeOrBooked']} {row['price']}" for row in Chambres]) or print("There are no rooms", '-'*50, sep="\n"))
#old code
    '''if len(Chambres) == 0:
        print("There are no rooms",'-'*50,sep="\n")
        return
    for row in Chambres:
        print(f"{row['num']} {row['numOfBeds']} {row['freeOrBooked']} {row['price']}",sep="\t")
    print('-' * 50)'''

#function for adding room manually
def AddRoomManually(Chambres):
    while True:
        try:
            num = int(input("Enter room number: "))
            break
        except ValueError:
            print("Please enter a valid integer")
            continue
    while True:
        try:
            numOfBeds = int(input("Enter number of beds: "))
            break
        except ValueError:
            print("Please enter a valid integer")
            continue
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Please enter a valid float")
            continue
    while True:
        try:
            freeOrBooked = input("Enter free or booked: ")
            if freeOrBooked.lower() not in ['free', 'booked']:
                raise ValueError
            break
        except ValueError:
            print("Please enter free or booked")

    Chambres.append({'num': num, 'numOfBeds': numOfBeds, 'freeOrBooked': freeOrBooked, 'price': price});Chambres.sort(key=lambda x: x['num']);DisplayAll(Chambres)
    
#function for deleting a room by number
def DeleteRoom(Chambres):
    while True:
        try:
            num = int(input("Enter room number: "))
            break
        except ValueError:
            print("Please enter a valid integer")
            continue
    if num not in [row['num'] for row in Chambres]:
        print("Room doesn't exist")
        return
    for row in Chambres:
        if row['num'] == num:
            Chambres.remove(row)
    DisplayAll(Chambres)

#function for saving rooms list to a txt file called Hotel.txt
def SaveToTextFile(Chambres):
    with open('Hotel.txt','w') as file:
        for row in Chambres:
            file.write(f"{row['num']} {row['numOfBeds']} {row['freeOrBooked']} {row['price']}\n")
    print("Rooms list saved to Hotel.txt")





#--------------------------------------------Main Code--------------------------------------------
#initialization of the dictionary
num= ''
numOfBeds = ''
freeOrBooked = ''
price = ''
#hotel room management dictionary: 
Chambre={'num':num, 'numOfBeds':numOfBeds, 'freeOrBooked':freeOrBooked, 'price':price}
Chambres =[]

#--------------------------------------------Menu--------------------------------------------
while True:
    print('-'*50)
    print("A. Add  random rooms")
    print("1. Display all rooms")
    print("2. Delete a room by number")
    print("3. Add a room manually")
    print("4. Save rooms to a text file")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice.lower() == 'a':
        AddRooms(Chambres)
    elif choice == '1':
        DisplayAll(Chambres)
    elif choice == '2':
        DeleteRoom(Chambres)
    elif choice == '3':
        AddRoomManually(Chambres)
    elif choice == '4':
        SaveToTextFile(Chambres)
    elif choice == '5':
        break
    else:
        print("Invalid choice")

