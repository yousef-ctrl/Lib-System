import datetime
import library_systems
import users_systems
import os
import time
data    =   users_systems.RegisterUser()
login   =   []

while True:
    if login:
        choose  =   []
        # Design of Interface (Library)

        print("\n"*30)
            ## Title

        print("-"*70)
        print(("Welcome, " + login[0]["name"] + " " + login[0]["surname"] + f" ({login[0]['role']})").center(70))
        print(str(datetime.datetime.strftime(datetime.datetime.now(),"%x")).ljust(70,"-"))

        
            ## Input Options 
        if login[0]["role"] == "Admin":
            options =   "\n" + "Browse Your Library -1".rjust(70) + "\n" + "Search With Writer Of The Book And Name -2".rjust(70) + "\n" + "Search With Just Name Of The Book -3".rjust(70) + "\n" + "Search With Just Writer Of The Book -4".rjust(70) + "\n" + "Add A Book In Your Library -5".rjust(70) + "\n" + "Logout -6".rjust(70) + "\n" + "Remove Your Account - 7".rjust(70) + "\n" + "Exit The System -8".rjust(70) + "\n" + "Remove A Book -9".rjust(70) + "\n" + "Clear The Library -10".rjust(70) + "\n" +"Admin Page -11".rjust(70)
            print(options)
        else:
            options =   "\n" + "Browse Your Library -1".rjust(70) + "\n" + "Search With Writer Of The Book And Name -2".rjust(70) + "\n" + "Search With Just Name Of The Book -3".rjust(70) + "\n" + "Search With Just Writer Of The Book -4".rjust(70) + "\n" + "Add A Book In Your Library -5".rjust(70) + "\n" + "Logout -6".rjust(70) + "\n" + "Remove Your Account - 7".rjust(70) + "\n"+ "Exit The System -8".rjust(70)
            print(options)
        print("\n"*15)
        choose.append(input("\nChoose An Option: "))

        print("-"*70)


        # Seçenekler

        if choose[0] == "1":
            with open("library_database.txt", "r", encoding="utf-8") as f:
                books   =   f.readlines()
                if books:
                    for x, i in enumerate(books):
                        print(f"{x+1}- {i.title()}")
                        print("\n")
                    input("")
                    continue
                else:
                    print("Your Library Doesn't Have A Book.")
                    time.sleep(1)
                    continue
        
        elif choose[0] == "2":
            choose.append(input("Write A Book For Search In The Library (Example. writer - name): "))
            if library_systems.search(choose[1].lower())[0]:
                print(f"\n {choose[1].title()} Is In Your Library.\n")
                print(f">>> The Searching Process Took {library_systems.search(choose[1].replace('I','ı').replace('İ','i').lower())[1]} Seconds.")
                time.sleep(2)
                continue
            else:
                print(f"\n>>> {choose[1].title()} Isn't In The Library.\n")
                time.sleep(1)
                continue

        elif choose[0] == "3":
            choose.append(input("Write Name Of The Book For Searching: "))
            if library_systems.searchName(choose[1].replace("I","ı").replace("İ","i").lower())[0]:
                print(f"\nThe Books That You Are Searching:\n")
                for i in library_systems.searchName(choose[1].replace("I","ı").replace("İ","i").lower())[0]:
                    print(f"- {i.title()}")
                print(f"\n>>> The Searching Process Took {library_systems.searchName(choose[1].replace('I','ı').replace('İ','i').lower())[1]} Seconds.")
                input("")
                continue
            else:
                print(f"\n>>> {choose[1].title()} Isn't The Library.\n")
                time.sleep(1)
                continue

        elif choose[0] == "4":
            choose.append(input("Write The Writer For Searching: "))
            if library_systems.searchWriter(choose[1].replace("I","ı").replace("İ","i").lower())[0]:
                print(f"\nBooks Of Writer That You Are Searching :\n")
                for i in library_systems.searchWriter(choose[1].lower())[0]:
                    print(f"- {i.title()}")
                print(f"\n>>> The Searching Process Took {library_systems.searchName(choose[1].replace('I','ı').replace('İ','i').lower())[1]} Seconds.")
                input("")
                continue
            else:
                print(f"\n>>> {choose[1].title()} Isn't In The Library.\n")
                time.sleep(1)
                continue

        elif choose[0] == "5":
            choose.append(input("Writer Of The Book: "))
            choose.append(input("Name Of The Book: "))
            library_systems.install(library_systems.Book(choose[1], choose[2]))
            print("\nThe Book Added To The Library Successfully.")
            time.sleep(1)
            continue

        elif choose[0] == "6":
            choose.append(input("Are You Sure For Logout? (y/n)"))
            if choose[1] == "y":
                login.clear()
                continue
            elif choose[1] == "n":
                print("The Process Canceled...")
                time.sleep(1)
                continue
            else:
                print("Undefined Option")
                time.sleep(1)
                continue

        elif choose[0] == "7":
            choose.append(input("Are You Sure For Remove Your Account From The System? (y/n)"))
            if choose[1] == "y":
                data.removeUser(users_systems.User(login[0]["name"], login[0]["surname"], login[0]["nickname"], login[0]["password"], login[0]["role"]))
                print("The Account Is Removing From The System...")
                login   =   []
                time.sleep(1)
                continue
            elif choose[1] == "n":
                print("The Process Canceled...")
                time.sleep(1)
                continue
            else:
                print("Undefined Value.")
                time.sleep(1)
                continue
        elif choose[0] == "8":
            print("The System Is Closing...")
            quit()
        
        if login[0]["role"] == "Admin":
            if choose[0] == "9":
                choose.append(input("Writer Name Of The Book: "))
                choose.append(input("Name Of The Book: "))
                edit    =   f"{choose[1].replace('I','ı').replace('İ','i').lower()} - {choose[2].replace('I','ı').replace('İ','i').lower()}"
                try:
                    library_systems.removelines(edit)
                except ValueError:
                    print(f"'{choose[1].title()} - {choose[2].title()}' Isn't In The Library.")
                    time.sleep(1)
                else:
                    print(f"'{choose[1].title()} - {choose[2].title()}' Removed From The Library.")
                    time.sleep(1)
                    continue

            elif choose[0] == "10":
                choose.append(input("Are You Sure For Clear The Library? (y/n)"))
                if choose[1] == "y":
                    with open("library_database.txt", "w"):
                        pass
                    print("The Process is Successful")
                    time.sleep(1)
                    continue
                elif choose[1] == "n":
                    print("The Process Canceled...")
                    time.sleep(1)
                    continue
                else:
                    print("Undefined Option")
                    time.sleep(1)
                    continue

            elif choose[0] == "11":
                while True:
                    choose  =   ["11"]
                    print("\n"*30)
                    print("Admin Page".center(70,"-"))
                    options1    =   "\n" + "See The Users -1".rjust(70) + "\n" + "Change Role Of A User -2".rjust(70) + "\n" + "Remove A User -3".rjust(70) + "\n" + "Go Back To The Library (...) -4".rjust(70)
                    print(options1)
                    print("\n"*15)
                    choose.append(input("\nChoose An Option: "))

                    if choose[1] == "1":
                        if not (data.users == login):
                            for i in data.users:
                                if i == login[0]:
                                    continue
                                else:
                                    print(f"\nName: {i['name']}")
                                    print(f"Surname: {i['surname']}")
                                    print(f"Nickname: {i['nickname']}")
                                    print(f"Role of the User: {i['role']}")
                                    print("*"*30)

                            input("")        
                            continue
                        else:
                            print("There Isn't A User.")
                            time.sleep(1)
                            continue

                    elif choose[1] == "2":
                        if not (login == data):
                            choose.append(input("Write A Nickname For Change His/Her Role: "))
                            for i in data.users:
                                if choose[2] == i["nickname"]:
                                    choose[2]   =   users_systems.User(i["name"], i["surname"], i["nickname"], i["password"], i["role"])
                                    pass
                                    break
                            else:
                                print("\nUndefined User")
                                time.sleep(1)
                                continue
                            choose.append(input("Write A Role ('Admin' or 'User'): "))
                            try:
                                data.changeRole(choose[2], choose[3])

                            except ValueError:
                                print("\nUndefined User")
                                time.sleep(1)
                                continue
                            else:
                                print(f"{choose[2].__dict__['nickname']} Changed To {choose[3]}.")
                                time.sleep(1)
                                continue
                                
                        else:
                            print("\nThere Isn't A User.")
                            time.sleep(1)
                            continue

                    elif choose[1] == "3":
                        if not (login == data):
                            choose.append(input("Write A Nickname For Remove From The System: "))
                            for i in data.users:
                                if choose[2] == i["nickname"]:
                                    choose[2]   =   users_systems.User(i["name"], i["surname"], i["nickname"], i["password"], i["role"])
                                    pass
                                    break
                            else:
                                print("\nUndefined User")
                                time.sleep(1)
                                continue
                                
                            data.removeUser(choose[2])
                            print(f"{choose[2].__dict__['nickname']} Removed From The System.")
                            time.sleep(1)
                            continue
                            
                        else:
                            print("\nThere Isn't A User.")
                            time.sleep(1)
                            continue

                    elif choose[1] == "4":
                        print("You Are Going Back To The Library...")
                        break
                continue
                        
        else:
            print("Undefined Option.")
            time.sleep(1)
            continue
            
    else:
        # Arayüz Tasarım (Kullanıcı)
        print("\n"*30)
            
            ## Başlık
        choose  =   []
        print(str(datetime.datetime.strftime(datetime.datetime.now(),"%x")).ljust(70,"-"))

            ## Seçenekler
            
        options =   "\n" + "Login -1".rjust(70) + "\n" + "Register -2".rjust(70) + "\n" + "Exit The System -3".rjust(70)
        print(options)
        print("\n"*15)
        choose.append(input("\nChoose An Option: "))

            ## Alt Sınır
        print("-"*70)

        # Seçenekler
            
        if choose[0] == "1":
            choose.append(input("Your Nickname: "))
            choose.append(input("Your Password: "))
            for i in data.users:
                if choose[1].strip() == i["nickname"]:
                    if choose[2] == i["password"]:
                        print("\nYou Did Login Successfully.")
                        login.append(i)
                        time.sleep(1)
                        break
                    else:
                        print("\nWrong Your Nickname Or Your Password!")
                        time.sleep(1)
                        break
                    
            else:
                print("\nWrong Your Nickname Or Your Password!")
                time.sleep(1)
                continue
            
        elif choose[0] == "2":
            choose.append(input("Your Name: "))
                                
            choose.append(input("Your Surname: "))
                            
            choose.append(input("Your Nickname (It must be unique): "))
            if choose[3].isalnum():
                liste   =   []
                for i in data.users:
                    if i["nickname"] == choose[3]:
                        liste.append(1)
                        print("The Nickname Already Exists. Please, Choose Another Nickname.")
                        break
                if liste:
                    time.sleep(1)
                    continue
            else:
                print("Please, Write Your Nickname With Just Alphanumeric Characters.")
                time.sleep(1)
                continue
                
            choose.append(input("Your Password: "))

            if len(choose[4])>=8:
                pass
            else:
                print("Your Password Must Be Least Eight (8) Characters.")
                time.sleep(1)
                continue
                    
            user    =   users_systems.User(choose[1], choose[2], choose[3], choose[4], "user")
            users_systems.RegisterUser().registration(user)
            data.users.append(user.__dict__)
            print("You Completed The Registration Process Successfully. Please, Login Now.")
            time.sleep(1)

        elif choose[0] == "3":
            print("The System Is Closing...")
            quit()
