import time
'''
The module communicates between the main file and "library_database.txt".
'''
class Book:
    '''
    The class edit your books with a special form.
    '''
    def __init__(self, writer, name):
        '''
        You must write a writer and a name for your books. First parameter is writer of book and second parameter is name of book.
        '''
        self.name   =   name
        self.writer =   writer
        self.edited()

    def edited(self):
        return self.writer.lower() + " - " + self.name.lower() + "\n"

def decorator(func):
    '''
    It calculate time of the process. It's a decorator function. 
    '''
    def wrapper(obj):
        start   =   time.time()
        func(obj)
        end     =   time.time()
        result  =   (end-start)
        return [func(obj),result]
    return wrapper

def install(bookobj):
    '''
    Its parameter must be a book object. Book object is adding with this method in "library database.txt".
    '''
    with open("library_database.txt", "a", encoding="utf-8") as file:
        file.write(bookobj.edited())
    sort()

@decorator
def search(obj):
    '''
    This method search its parameter that must be a string in "library_database.txt". Result of the searching is a list data.
    First index of the list is boolean and second index of the list is float because the second index is time of the searching.
    You can use for search your book with its writer and its name.
    '''
    with open("library_database.txt", "r", encoding="utf-8") as file:
        liste   =   file.readlines()
        for i in liste:
            if i == (obj.lower().strip() + "\n"):
                return True
        else:
            return False
def removelines(obj):
    '''
    Its parameter must be a string. It remove the value in "database_library.txt".
    '''
    with open("library_database.txt", "r", encoding="utf-8") as file:
        liste   =   file.readlines()
    obj     =   obj+"\n"
    liste.remove(obj)
    with open("library_database.txt", "w+", encoding="utf-8") as file:
        for i in liste:
            file.write(i)

def sort():
    '''
    The method alphabetic sort the books.
    '''
    with open("library_database.txt", "r", encoding="utf-8") as file:
        liste   =   file.readlines()
        liste.sort()
        
    with open("library_database.txt", "w+", encoding="utf-8") as file:
        file.writelines(liste)

@decorator
def searchName(obj):
    '''
    This method search its parameter that must be a string in "library_database.txt". Result of the searching is a list data.
    First index of the list is False or a list and second index of the list is float because the second index is time of the searching.
    Result of searching is unsuccessful if first index is False. If first index is a list Your result of searching is successful and the list is your result. 
    You can use for search your book with just its name.
    '''
    with open("library_database.txt", "r", encoding="utf-8") as file:
        liste   =   file.readlines()
        results =   []
        for i in liste:
            i   =   i.split(" - ")
            if ( i[1] == (obj.lower().strip() + "\n") ):
                results.append(" - ".join(i))
        if results==[]:
            return False
        else:
            return results

@decorator
def searchWriter(obj):
    '''
    This method search its parameter that must be a string in "library_database.txt". Result of the searching is a list data.
    First index of the list is False or a list and second index of the list is float because the second index is time of the searching.
    Result of searching is unsuccessful if first index is False. If first index is a list Your result of searching is successful and the list is your result. 
    You can use for search your book with just its writer.
    '''
    with open("library_database.txt", "r", encoding="utf-8") as file:
        liste   =   file.readlines()
        results =   []
        for i in liste:
            i   =   i.split(" - ")
            if ( i[0] == (obj.lower().strip()) ):
                results.append(" - ".join(i))
        if results==[]:
            return False
        else:
            return results

