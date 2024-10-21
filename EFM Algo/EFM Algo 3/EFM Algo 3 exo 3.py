#--------------------------------------------Modules--------------------------------------------
import faker,random
fake = faker.Faker('en-US')
#---------------------------------------------------------------------------------------------
#--------------------------------------------Functions--------------------------------------------
#fucntion to sort members by number
def sortMembers():
    T.sort(key=lambda x: x['num'])

#function to display members
def displayMembers():
    for i in T:
        print({'num': i['num'], 'activity': i['activity'], 'full name': i['full name'], 'adress': i['adress']})
    print('-'*20)    

#function to add members
def addMembers():
    #ask user for the number of members to add
    try:
        n=int(input('Enter the number of members: '))
    except:
        print("Please enter a valid integer")
    for i in range(1,n+1):
        T.append({'num':random.randint(1,10000000) if num not in [row['num'] for row in T] else random.randint(1,10000000) , 'activity': random.choice(activities), 'full name': fake.name(), 'adress': fake.address()})
        
    sortMembers()
    displayMembers()

#function to add member manually
def addMemberManually():
    while True:
        try:
            n=int(input('Enter the number of the new member: '))
            if n in [row['num'] for row in T]:
                print('The member already exists')
                continue
            break
        except:
            print("Please enter a valid integer")
    T.append({'num':n, 'activity':input('Enter the activity of the new member: '), 'full name':input('Enter the full name of the new member: '), 'adress':input('Enter the adress of the new member: ')})
    sortMembers()
    print('The new member has been added successfully')
    displayMembers()

#function to delete member by number
def deleteMemberByNum():
    while True:
        try:
            n=int(input('Enter the number of the member to delete: '))
            if n not in [row['num'] for row in T]:
                print('The member does not exist')
                continue
            break
        except:
            print("Please enter a valid integer")
    T.remove(member['num'] == n)    
    print('The member has been deleted successfully')
    displayMembers()
       

#fucntion to save T in a text file named 'adhérents.txt'
def saveMembers():
    with open('adhérents.txt', 'w') as file:
        for i in T:
            file.write(f'{i["num"]} {i["activity"]} {i["full name"]} {i["adress"]}\n')
    print('Members saved successfully')

#------------------------------------------------Main Code--------------------------------------------
#iniialization of the dictionary
num = ''
activity = ''
fullName = ''
adress = ''
#defining the structure of the dictionary
member={'num': num, 'activity': activity, 'full name': fullName, 'adress': adress}
#initialization of the list
T=[]
#list of available activities
activities = [
    'Hiking',
    'Traveling',
    'Reading',
    'Painting',
    'Playing guitar',
    'Cooking',
    'Gardening',
    'Photography',
    'Cycling',
    'Swimming',
    'Team sports',
    'Yoga',
    'Meditation',
    'Learning a new language',
    'Volunteering',
    'Attending concerts',
    'Trying new foods',
    'Watching movies',
    'Playing video games'
]


#--------------------------------------------Menu--------------------------------------------
while True:
    print('-'*50)
    print("A. Add  random members")
    print("1. Display all members")
    print("2. Add a member manually")
    print("3. Delete a member by number")
    print("4. Save members to a text file")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice.lower() == 'a':
        addMembers()
    elif choice == '1':
        displayMembers()
    elif choice == '2':
        addMemberManually()
    elif choice == '3':
        deleteMemberByNum()
    elif choice == '4':
        saveMembers()
    elif choice == '5':
        break