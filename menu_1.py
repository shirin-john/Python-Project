#program for login/new member

import getconn
from new_member_ import n_member as new
from emoji import emojize as e

while True:
    print("_" * 130)
    print(e("\t\t\t:books::child: LITTLE READERS :child::books:"))

    print("\n1. Login \n2. Add Member")
    ch_1 = int(input("\nPlease Enter Your Choice: "))

    n = new()

#login
    if ch_1 == 1:
        
        print("_" * 130)
        print(e(":bookmark: Login To Your Account:"))
        
        usern = input("\nEnter Your Username: ")
        passw = int(input("Enter Your Password: "))
        
        sql  = "select * from readers"
        mydb = getconn.getconn()
        mycur = mydb.cursor()
        mycur.execute(sql)
        records = list(mycur.fetchall())

        list_1 = [] #for usernames
        list_2 = [] #for passwords

        for r in records:
            list_1.append(r[0])
            list_2.append(r[-3])

        list_3 = dict(zip(list_1,list_2)) #username-password dictionary
        
        for u,p in list_3.items():
            if usern == u and passw == p:
                print("Logged In\n")
                import menu_2
                break
            else:
                print("Invalid Input. Please Try Again\n")
            
            
            
            
    #adding new member
    elif ch_1 == 2: 
        n.add_member()
        

    else:
        print("Invalid Choice. Please Try Again.")
        break


        




