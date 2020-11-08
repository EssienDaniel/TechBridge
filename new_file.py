import datetime
class User():
    def __init__(self, name):
        self.name = name

class Notepad:
    def __init__(self, user):
        self.body = ""
        self.title = ""
        self.user = user

    def create_note(self):  #THIS FUNCTION CREATES THE NOTES
        title = input("Please enter your note title: ")
        body = input("Please enter your note body: ")
        username = self.user.name

        note = f"{title}, {body}, {username} \n"
        self.store_note(note)

    def store_note(self, note):
        file = open("notes.csv", "a")
        file.write(note)
        file.close()


# THIS FUNCTION ALLOWS YOU TO READ ALL NOTES

    def read_notes(self):
        file = open("notes.csv")
        data = file.read()

        print(f"date".center(30), f"name".center(13), f"title".center(21), f"body".center(26), sep = " | " )
        print(f"-" * 100)
        
        for line in data.splitlines():
            #print("-" * 40)
            #print(line)
            
            individual_components = line.split(",")
            #print(individual_components)
            
            title, body, name = individual_components
            today = datetime.datetime.now()
            print(f"{today}".center(30), f"{name}".center(13), f"{title}".center(21), f"{body}".center(26), sep = " | " )

# THIS FUNCTION ALLOWS YOU TO READ PNLY ONE PERSON'S NOTES

    def read_personal_notes(self):
        file = open("notes.csv")
        data = file.read()

        print(f"date".center(15), f"name".center(13), f"title".center(21), f"body".center(26), sep = " | " )
        print(f"-" * 80)

        for line in data.splitlines():
            individual_components = line.split(",")
            title, body, name = individual_components
            
            if name.strip() == self.user.name.strip():
                today = datetime.datetime.now()
                print(f"{today}".center(15), f"{name}".center(13), f"{title}".center(21), f"{body}".center(26), sep = " | " )
            # else:
            #     print("Not found")

name = input("Please enter your name: ")
me = User(name = name)
my_notepad = Notepad(me)
#my_notepad.create_note()
my_notepad.read_notes()
#my_notepad.read_personal_notes()