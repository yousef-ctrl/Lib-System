import json
import os
'''
The module include special classes and methods for to save library users.
'''
class User:
    '''
    The class define your users in a special form 
    '''
    def __init__(self, name, surname, nickname, password, role):
        self.name       =   name.title()
        self.surname    =   surname.upper()
        self.nickname   =   nickname.lower()
        self.password   =   password
        self.role       =   role.title()
        self.checkRole()

    def checkRole(self):
        '''
        The method check true or false of your user role. 
        '''
        if not (self.role == "Admin" or self.role == "User"):
            raise ValueError("Please, choose 'Admin' or 'User' role.")

class RegisterUser:
    '''
    Aim of the class is to copy data in the json file.
    
    '''
    def __init__(self):
        self.users	=	[]
        self.accessFile()
        
    
    def accessFile(self):
        if not os.stat("users_database.json").st_size == 0:
            with open("users_database.json", "r", encoding="utf-8") as file:
                data    =   json.load(file)
                for i in list(data):
                    self.users.append(i)
        else:
            pass

    def preRegister(self, user: User):
        self.users.append(user.__dict__)

    def registration(self, user: User):
        '''
        You can do register process with this method but the process must do after the class definition because you must copy in this python file the data that in the json file.
        '''
        self.preRegister(user)
        with open("users_database.json", "w", encoding="utf-8") as file:
            json.dump(self.users, file)

    def removeUser(self, user: User):
        '''
        You can remove a user with this method.
        '''
        liste   =   []
        for i in self.users:
            if not i == user.__dict__:
                liste.append(i)
            else:
                continue
        self.users  =   liste.copy()
        with open("users_database.json", "w", encoding="utf-8") as file:
            json.dump(self.users, file)
       

    def changeRole(self, user: User, role):
        '''
        You can change role of a user.
        '''
        role    =   role.title()
        if not (role == "Admin" or role == "User"):
            raise ValueError("Undefined role.")
        else:
            for i in self.users:
                if i["nickname"] == user.nickname:
                    i["role"]   =  role
        with open("users_database.json", "w", encoding="utf-8") as file:
            json.dump(self.users, file)

