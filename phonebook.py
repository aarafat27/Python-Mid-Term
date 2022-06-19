phone_book={}
p1={'name':'Arafat', 'Address':'Dhaka','Email':'arafatedu11@gmail.com','Phone_no':['01098', '091234']}
p2={'name':'Mehrab', 'Address':'Chittagong','Email':'mehrab@gmail.com','Phone_no':['01034', '035234']}
p3={'name':'Rifat', 'Address':'Manikgonj','Email':'rifat@gmail.com','Phone_no':['01748', '457864']}
p4={'name':'Tobarak', 'Address':'Noakhali','Email':'tobarak@gmail.com','Phone_no':['01098', '091234']}
list_conct=[p1,p2,p3,p4]
for i in range(1,len(list_conct)+1):
    phone_book[i]= list_conct[i-1]



def display(phone_book):
    '''This function display all the contact in the phonebook'''
    print('\n*-*-*-*-*-* All the contact list *-*-*-*-*-*')
    temp = len(phone_book)
    for key ,value in phone_book.items():
        print("User no :",key)
        for k,v in value.items():
            print(k+": ",v)
        print('\n')
    menu()  
    
def add_user(phone_book):
    '''This function add new contact in the phonebook'''
    phone_books={}
    phone_no=[]
    phn_no=' '
    name =input("Please enter name: ")
    name = name.title()
    address =input("Please enter address: ")
    email =input("Please enter email: ")
    print("Please enter Phone no: ", end ='')
    while phn_no != '':
        phn_no = input()
        phone_no.append(phn_no)

    phone_books['Name']= name
    phone_books['Address']= address
    phone_books['Email']= email
    phone_books['Phone_no']= phone_no[:-1]
    temp = len(phone_book)
    phone_book[temp+2]= phone_books
    print("New contact added successfully!")
    store(phone_book)
    
    
def search(phone_book):
    '''This function search for contact in contact list'''
    found = False
    name=input("Enter name to search :")
    name=name.title()
    for key ,value in phone_book.items():
        for k in value.values():
            if(k==name):
                print('Found!')
                for i,j in phone_book[key].items():
                    print(i+": ",j)
                found =True
                menu()
        
    if found == False:
        print("There's no contact Record in Phone Book with name = " + name )
        msg = input("Want to add new contact? [y or n]")
        msg=msg.lower()
        if msg == 'y':
            add_user(phone_book)
        else:
            menu()
            


def update(phone_book):
    '''This function update contact in the phonebook'''
    found = False
    name=input("Enter name to update :")
    name=name.title()
    for key ,value in phone_book.items():
        for k in value.values():
            if(k==name):
                print('Found!')
                for i,j in phone_book[key].items():
                    print(i+": ",j)
                temp = input('\nWhat to update?\n1.Name\n2.Address\n3.Email\n4.Phone no\n')
                if temp == '1':
                    new_name=input('Enter name :')
                    phone_book[key]['name']=new_name
                if temp == '2':
                    new_add=input('Enter address :')
                    phone_book[key]['Address']=new_add
                if temp == '3':
                    new_email=input('Enter Email :')
                    phone_book[key]['Email']=new_email
                if temp == '4':
                    phone_no=[]
                    phn_no=' '
                    print('Enter new Phone no :',end ='')
                    while phn_no != '':
                        phn_no = input()
                        phone_no.append(phn_no)
                    phone_book[key]['Phone_no']= phone_no[:-1]
                found =True
                store(phone_book)
                break
    
    if found == False:
        print("There's no contact Record in Phone Book with name = " + name )
        msg = input("Want to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            update(phone_book)
        else:
            menu()


def delete(phone_book):
    '''This function delete contact in the phonebook'''
    found = False
    t= 0
    name=input("Enter name to delete :")
    name=name.title()
    for key ,value in phone_book.items():
        for k in value.values():
            if(k==name):
                print('Found!')
                temp = input("Are you sure you want to delete? [Y or N] : ")
                temp=temp.title()
                if temp == 'Y':
                    t = key  
                found =True
            
    if t != 0:
        del phone_book[t]
        print('Contact deleted successfully!')
        display(phone_book)
    if found == False:
        print("There's no contact Record in PhoneBook with name : " + name )
        msg = input("Want to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            delete(phone_book)
        else:
            menu()


def store(phone_book):
     '''This function save all the contact of Phonebook in a text file'''
     with open("phonebook.txt", 'w') as pb:
         for value in phone_book.values():
             pb.write(str(value))
             pb.write("\n")
     print( "All the contact saved successfully!")
     display(phone_book)


def menu():
    msg = '''\n   ****************** PhoneBook ****************\n
            Supervised by Akinul Islam Jony
          --------------------------------------\n
          Enter 1,2,3,4,5,6 or 7:\n
          Enter 1 To Display All Contacts Records\n 
          Enter 2 To Add a New Contact Record\n
          Enter 3 To Search your contacts\n
          Enter 4 To Update your contacts\n
          Enter 5 To Delete your contacts\n
          Enter 6 To Store your contacts\n
          Enter 7 To Quit\n
         ---------------------------------------\n'''
    print(msg)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        display(phone_book)
        
    elif user_input == "2":
        add_user(phone_book)
        
    elif user_input == "3":
        search(phone_book)
        
    elif user_input == "4":
        update(phone_book)
        
    elif user_input == "5":
        delete(phone_book)
        
    elif user_input == "6":
        store(phone_book)
        
    elif user_input == "7":
        print("Thanks for using PhoneBook")

    else:
        print("Wrong choice, Please Enter [1 to 7]\n")
        temp = input("Press Enter to continue ...")
        menu()
  

menu()
