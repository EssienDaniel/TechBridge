from time import time, ctime
import math

# ##  A SET OF CLASSES THAT ACT LIKE A USER'S NOTEPAD BUT CAN ONLY WRITE

# class User():

#     def __init__(self, name):
#         self.name = name

# class Notepad:
    
#     def __init__(self, user):

#         self.body = ""
#         self.title = ""
#         self.time = ctime(time())
#         self.user = user

#     def create_note(self):

#         title = input("Please enter your note title : ")
#         body = input("Please enter your note body : ")
#         username = self.user.name

#         note = f"{title},{body},{username},{self.time}\n"

#         self.store_note(note)

#     def store_note(self, note):

#         file = open("notes.csv", "a")
#         file.write(note)
#         file.close()

# name = input("Please enter your name : ")
# me = User(name= name)

# my_notepad = Notepad(me)

#my_notepad.create_note()


#  A SET OF CLASSES THAT ACT LIKE A USER'S NOTEPAD AND ALLOW FOR READ AND WRITE

class User():
    
    def __init__(self, name):
        self.name = name
        

class Notepad:
    
    def __init__(self, user):

        self.body = ""
        self.title = ""
        self.time = ctime(time())
        self.user = user


    def create_note(self):

        title = input("Please enter your note title : ")
        body = input("Please enter your note body : ")
        username = self.user.name

        note = f"{title},{body},{username},{self.time}\n"

        self.store_note(note)

    def store_note(self, note):

        file = open("notes.csv", "a")

        file.write(note)
        file.close()

    #THIS FUNCTION ALLOWS YOU TO READ ALL NOTES
    def read_notes(self):

        file = open("notes.csv")

        data = file.read()
        
        print(f"name".center(8), f"title".center(21), f"body".center(16), f"time".center(25), sep= " | ")
        print(f"-"*80)
        for line in data.splitlines():
            
            print("-"*40)
            print(line)
            print()
            individual_components = line.split(",")
            print(individual_components)

            title, body, name, time = individual_components

            print(f"{name}".center(8), f"{title}".center(21), f"{body}".center(30), f"{time}".center(25), sep= " | ")
    
    #THIS FUNCTION ALLOWS YOU TO READ ONLY ONE PERSON'S NOTES
    
    def read_personal_notes(self):

        file = open("notes.csv")

        data = file.read()
        
        print(f"name".center(8), f"title".center(21), f"body".center(30),f"time".center(20), sep= " | ")
        print(f"-"*80)
        for line in data.splitlines():
            
            individual_components = line.split(",")

            title, body, name, time  = individual_components

            if name.strip() == self.user.name.strip():

                print(f"{name}".center(8), f"{title}".center(21), f"{body}".center(30), f"{time}".center(20), sep= " | ")

        

            

name = input("Please enter your name : ")
me = User(name= name)

my_notepad = Notepad(me)

#my_notepad.create_note()
my_notepad.read_notes()
#my_notepad.read_personal_notes()





