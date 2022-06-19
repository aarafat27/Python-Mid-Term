k1d='''
    if is used for conditional branching or decision making.
    When we want to test some condition and execute a block only
    if the condition is true, then we use if
    '''

k1s='''
   def if_example(a):
       if a == 1:
           print('One')
       elif a == 2:
           print('Two')
       else:
           print('Something else')

   if_example(2)
   if_example(4)
   if_example(1)

   Output:

   Two
   Something else
   One
   '''

k2d='''
    del is used to delete the reference to an object.Everything
    is object in Python. We can delete a variable reference using del
    '''

k2s= '''
 >>> a = ['x','y','z']
 >>> del a[1]
 >>> a
 ['x', 'z']
 '''

k3d='''
   class is used to define a new user-defined class in Python.
   Class is a collection of related attributes and methods that try to
   represent a real-world situation.This idea of putting data and f
   unctions together in a class is central to the concept of
   object-oriented programming (OOP).
'''

k3s='''
  class ExampleClass:
      def function1(parameters):
          …
      def function2(parameters):
          …
    '''

k1 = {'keyword':'if','description':k1d ,'sample':k1s }
k2 = {'keyword':'del','description':k2d,'sample':k2s }
k3 = {'keyword':'class','description':k3d,'sample':k3s }

keywords=[k1,k2,k3]

def display(keywords):
    '''This function display all the keyword'''
    print('\n*-*-*-*-*-* All the keyword list *-*-*-*-*-*')
    temp = len(keywords)
    for i in keywords:
        for key ,value in i.items():
            print(key+": ",value)
        print('\n')
    menu()



def display_list(keywords):
    keywords_list=[]
    for i in keywords:
        for k,v in i.items():
            if k =='keyword':
                keywords_list.append(v)
    print('\nAvailable Keywords are: ', end='')
    for i in keywords_list:
        print(i,end='  ')
    t = input('\n\nWant to know more about specific keywords? [y or n] :')
    t=t.lower()
    if t=='y':
        search(keywords)
    else:
        menu()
        
    


def add_keyword(keywords):
    '''This function add new keyword'''
    new_keyword={}
    keyword =input("\nPlease enter python keyword: ")
    keyword = keyword.lower()
    description =input("\nPlease enter description: ")
    print("\nPlease enter sample: ",end ='')
    s=' '
    p=''
    while s!='':
        s=input()
        p=p+s

    sample=p
    

    new_keyword['keyword']= keyword
    new_keyword['description']= description
    new_keyword['sample']= sample

    keywords.append(new_keyword)
    print("\nNew keyword added successfully!")
    display(keywords)
    



def update(keywords):
    '''This function update keywords'''
    found = False
    keyword=input("\nEnter a keyword :")
    keyword=keyword.lower()
    for i in keywords:
        for k,v in i.items():
            if(v==keyword):
                print('\nFound!')
                for key,value in i.items():
                    print(key+": ",value)
                    
                temp = input('\nWhat to update?\n1.keyword\n2.Description\n3.sample\n')
                if temp == '1':
                    new_keyword=input('\nEnter Keyword :')
                    i['keyword']=new_keyword
                    
                if temp == '2':
                    new_desc=input('\nEnter Description :')
                    i['description']=new_desc
                if temp == '3':
                    new_sample=input('\nEnter sample :')
                    i['samplep']=new_sample
                print("\nUpdated!")
                found =True
                store(keywords)
    
    if found == False:
        print("There's no keyword name : " + keyword )
        msg = input("Want to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            update(keywords)
        else:
            menu()


def delete(keywords):
    '''This function delete keyword'''
    found = False
    t= 0
    keyword=input("Enter keyword to delete :")
    keyword=keyword.lower()
    for i in keywords:
        for k,v in i.items():
            if(v==keyword):
                print('Found!')
                for key,value in i.items():
                    print(key+": ",value)
                temp = input("\nAre you sure you want to delete? [Y or N] : ")
                temp=temp.title()
                if temp == 'Y':
                    t =i
                    found =True
                
                else:
                    menu()
            
    if t != 0:
        keywords.remove(t)
        print('\nKeyword deleted successfully!')
        display(keywords)
    if found == False:
        print("\nThere's no keyword named  " + keyword )
        msg = input("\nWant to try again? [y or n] :")
        msg = msg.lower()
        if msg=='y':
            delete(keywords)
        else:
            menu()

def search(keywords):
    '''This function search keywords'''
    found = False
    keyword=input("\nEnter keyword to search :")
    keyword=keyword.lower()
    for i in keywords:
        for k,v in i.items():
            if(v==keyword):
                print('\nFound!\n')
                for key,value in i.items():
                    print(key+": ",value)
                
                found =True
                t =input('Want to know about another keyword? [y or n] :')
                t=t.lower()
                if t=='y':
                    search(keywords)
                else:
                    menu()
        
    if found == False:
        print("There's no keyword named : " + keyword )
        msg = input("Want to add new keyword? [y or n] :")
        msg=msg.lower()
        if msg == 'y':
            add_keyword(keywords)
        else:
            menu()


def store(keywords):
     '''This function save all the keywords in a text file'''
     with open("keywords.txt", 'w') as kw:
         for i in keywords:
             kw.write(str(i))
             kw.write("\n")
             
     print( "\nAll the keywords saved successfully!")
     menu()



def menu():
    msg = '''\n\n     ************** Keyword List Application****************\n
            Supervised by Akinul Islam Jony
          --------------------------------------\n
          Enter 1,2,3,4,5,6,7 or 8:\n
          Enter-1: To Display All Keywords\n 
          Enter-2: To Add a New Keyword\n
          Enter-3: To Update keywords\n
          Enter-4: To See all keywords and description\n
          Enter-5: To Delete Keywords\n
          Enter-6: To Search Keyword\n
          Enter-7: To Store Keywords\n
          Enter-8: To Quit\n
         ---------------------------------------\n'''
    print(msg)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        display_list(keywords)
        
    elif user_input == "2":
        add_keyword(keywords)
        
    elif user_input == "3":
        update(keywords)
        
    elif user_input == "4":
        display(keywords)
        
    elif user_input == "5":
        delete(keywords)
        
    elif user_input == "6":
        search(keywords)
        
    elif user_input == "7":
        store(keywords)
        
    elif user_input == "8":
        print("Thanks for using Keywords list app")

    else:
        print("Wrong choice, Please Enter [1 to 8]\n")
        temp = input("Press Enter to continue ...")
        menu()
  
menu()
