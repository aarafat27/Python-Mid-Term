t1 = {'date':'7-Mar-22','description': "Attend a metting",'place':'Dhaka' }
t2 = {'date':'8-Mar-22','description': "Attend a Birthday", 'place':'Cumilla' }
t3 = {'date':'6-Mar-22','description': "Attend a Seminar", 'place':'AIUB' }
to_do=[t1,t2,t3]


def display(to_do):
    '''This function display all the task list from To-Do list'''
    print('\n*-*-*-*-*-* All the task list *-*-*-*-*-*')
    temp = len(to_do)
    for i in to_do:
        for key ,value in i.items():
            print(key+": ",value)
        print('\n')
    menu()

def sort(to_do):
    newlist=sorted(to_do, key=lambda k:k['date'])
    print("\nTask sorted according to date\n")
    for i in newlist:
        for key ,value in i.items():
            print(key+": ",value)
        print('\n')
    menu()


def immediate_task(to_do):
    newlist=sorted(to_do, key=lambda k:k['date'])
    print("\nImmediate next task is :\n")
    for key ,value in newlist[0].items():
        print(key+": ",value)
    print('\n')
    menu()


def add_task(to_do):
    '''This function add new task in the To-Do List'''
    new_task={}
    date =input("\nPlease enter date [ex: 7-Mar-22]: ")
    date = date.title()
    description =input("\nPlease enter description: ")
    place =input("\nPlease enter place: ")

    new_task['date']= date
    new_task['description']= description
    new_task['place']= place


    to_do.append(new_task)
    print("\nNew task added successfully!")
    display(to_do)
    store(to_do)


def update(to_do):
    '''This function update task in the To-Do list'''
    found = False
    date=input("\nEnter date to update[ex: 7-Mar-22] :")
    date=date.title()
    for i in to_do:
        for k,v in i.items():
            if(v==date):
                print('\nFound!')
                for key,value in i.items():
                    print(key+": ",value)
                    
                temp = input('\nWhat to update?\n1.Date\n2.Description\n3.Place\n')
                if temp == '1':
                    new_date=input('\nEnter Date :')
                    i['date']=new_date
                    
                if temp == '2':
                    new_desc=input('\nEnter Description :')
                    i['description']=new_desc
                if temp == '3':
                    new_place=input('\nEnter Place :')
                    i['place']=new_place
                print("\nUpdated!")
                found =True
                display(to_do)
    
    if found == False:
        print("There's no task Record in to do list with date : " + date )
        msg = input("Want to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            update(to_do)
        else:
            menu()


def delete(to_do):
    '''This function delete task in the to do list'''
    found = False
    t= 0
    date=input("Enter date to delete task :")
    date=date.title()
    for i in to_do:
        for k,v in i.items():
            if(v==date):
                print('Found!')
                for key,value in i.items():
                    print(key+": ",value)
                temp = input("\nAre you sure you want to delete? [Y or N] : ")
                temp=temp.title()
                if temp == 'Y':
                    t =i
                found =True
            
    if t != 0:
        to_do.remove(t)
        print('\nTask deleted successfully!')
        display(to_do)
    if found == False:
        print("\nThere's no task Record in to-do list on date " + date )
        msg = input("\nWant to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            delete(to_do)
        else:
            menu()



def store(to_do):
     '''This function save all the task of to-do list in a text file'''
     with open("todo.txt", 'w') as td:
         newlist=sorted(to_do, key=lambda k:k['date'])
         #print("\nTask sorted according to date\n")
         for i in newlist:
             td.write(str(i))
             td.write("\n")
             
     print( "\nAll the task saved successfully!")
     sort(to_do)



def menu():
    msg = '''\n     ************** To-Do Application****************\n
            Supervised by Akinul Islam Jony
          --------------------------------------\n
          Enter 1,2,3,4,5,6,7 or 8:\n
          Enter-1: To Display All Task List\n 
          Enter-2: To Add a New Task in To-Do\n
          Enter-3: To Update task in To-Do\n
          Enter-4: To Display Immediate Task\n
          Enter-5: To Delete Task\n
          Enter-6: To View Tasks According to Time\n
          Enter-7: To Store Tasks\n
          Enter-8: To Quit\n
         ---------------------------------------\n'''
    print(msg)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        display(to_do)
        
    elif user_input == "2":
        add_task(to_do)
        
    elif user_input == "3":
        update(to_do)
        
    elif user_input == "4":
        immediate_task(to_do)
        
    elif user_input == "5":
        delete(to_do)
        
    elif user_input == "6":
        sort(to_do)
        
    elif user_input == "7":
        store(to_do)
        
    elif user_input == "8":
        print("Thanks for using To-Do app")

    else:
        print("Wrong choice, Please Enter [1 to 8]\n")
        temp = input("Press Enter to continue ...")
        menu()
  

menu()
