#  CLASS OF ANIMAL WITH 3 METHODS OR POSSIBLE BEHAVIOURS
# class Animal:

#     def talk(self):
#         print ("I have something to say and thanks is what i say!")

#     def walk(self):
#         print ("Hey! I am walking here!")
        
#     def clothes(self):
#         print ("I have nice clothes!")


# new_animal = Animal()
# new_animal.talk()

# print(type(new_animal))


# #  CLASS OF ANIMAL WITH 3 METHODS OR POSSIBLE BEHAVIOURS, and 4 CLASS ATTRIBUTES
# class Animal:

#     # CLASS ATTRIBUTES
#     legs = True
#     hands = True
#     fins = False
#     fur = True

#     def talk(self):
#         print ("I have something to say and thanks is what i say!")

#     def walk(self):
#         print ("Hey! I am walking here!")
        
#     def clothes(self):
#         print ("I have nice clothes!")


# new_animal = Animal() # INSTANTIATION OF A CLASS ( THE CLASS Animal())
# new_animal2 = Animal()
# new_animal2.fur = False

# print(new_animal.fur)
# print(new_animal2.fur)

# # print(type(new_animal))


# #  CLASS OF ANIMAL WITH 3 METHODS OR POSSIBLE BEHAVIOURS 4 CLASS ATTRIBUTES 3 INSTANCE ATTRIBUTES
# class Animal:

#     # CLASS ATTRIBUTES
#     legs = True
#     hands = True
#     fins = False
#     fur = True

#     def __init__(self, name, age, height): # INITIALIZATION OF CLASS ATTRIBUTES.

#         self.name = name
#         self.age = age
#         self.height = height

#     def talk(self):
#         print ("I have something to say and thanks is what i say!")

#     def walk(self):
#         print ("Hey! I am walking here!")
        
#     def clothes(self):
#         print ("I have nice clothes!")

#     def describe_self(self):
    
#         print(f"Hello there my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.")
        


# animal1 = Animal(name = "bruno", age = 30, height = 5.7) # INSTANTIATION OF A CLASS ( THE CLASS Animal())
# animal2 = Animal(name = "tiger", age = 15, height = 4.7)

# # print(animal1.name)
# # print(animal2.name)

# # print(type(new_animal))

# animal2.describe_self()

#  CLASS OF ANIMAL WITH 4 METHODS OR POSSIBLE BEHAVIOURS 4 CLASS ATTRIBUTES 3 INSTANCE ATTRIBUTES
# class Animal:

#     # CLASS ATTRIBUTES
#     legs = True
#     hands = True
#     fins = False
#     fur = True

#     def __init__(self, name, age, height): # INITIALIZATION OF CLASS ATTRIBUTES.

#         self.name = name
#         self.age = age
#         self.height = height

#     def talk(self):
#         print ("I have something to say and thanks is what i say!")

#     def walk(self):
#         print ("Hey! I am walking here!")
        
#     def clothes(self):
#         print ("I have nice clothes!")

#     def describe_self(self):
    
#         print(f"Hello there my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.")

#     def say_hello(self, other_party):

#         iam_taller_than_other = True if other_party.height < self.height else False

#         if iam_taller_than_other:

#             print(f"Hello there {other_party.name}, my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.\nApparently you are taller than me.")
        
#         elif not iam_taller_than_other:

#             print(f"Hello there {other_party.name}, my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.\nApparently I am taller than you.")

        


# animal1 = Animal(name = "bruno", age = 30, height = 5.7) # INSTANTIATION OF A CLASS ( THE CLASS Animal())
# animal2 = Animal(name = "tiger", age = 15, height = 4.7)

# # print(animal1.name)
# # print(animal2.name)

# # print(type(new_animal))

# # animal2.describe_self()
# animal2.say_hello(animal1)

#  CLASS OF ANIMAL WITH 4 METHODS OR POSSIBLE BEHAVIOURS 4 CLASS ATTRIBUTES 3 INSTANCE ATTRIBUTES
# class Animal:

#     # CLASS ATTRIBUTES
#     legs = True
#     hands = True
#     fins = False
#     fur = True

#     def __init__(self, name, age, height): # INITIALIZATION OF CLASS ATTRIBUTES.

#         self.name = name
#         self.age = age
#         self.height = height

#     def talk(self):
#         print ("I have something to say and thanks is what i say!")

#     def walk(self):
#         print ("Hey! I am walking here!")
        
#     def clothes(self):
#         print ("I have nice clothes!")

#     def describe_self(self):
    
#         print(f"Hello there my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.")

#     def say_hello(self, other_party):

#         iam_taller_than_other = True if other_party.height < self.height else False

#         if iam_taller_than_other:

#             print(f"Hello there {other_party.name}, my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.\nApparently you are taller than me.")
        
#         elif not iam_taller_than_other:

#             print(f"Hello there {other_party.name}, my name is {self.name}, i am {self.age} years old, and i am {self.height}ft tall.\nApparently I am taller than you.")

#     def get_age(self):

#         return self.age
        


# animal1 = Animal(name = "bruno", age = 30, height = 5.7) # INSTANTIATION OF A CLASS ( THE CLASS Animal())
# animal2 = Animal(name = "tiger", age = 15, height = 4.7)

# print(animal1.get_age())

# print(animal1.name)
# print(animal2.name)

# print(type(new_animal))

# animal2.describe_self()
# animal2.say_hello(animal1)

# INHERITANCE AND POLYMORPHISM WITH PYTHON 

# class Dog(Animal):
#     type = "dog"
#     genus = "canine"

#     def __init__(self, name, age, height, color, bark_volume):
#         Animal.__init__(self, name, age, height) # INITIALIZING THE PARENT CLASS WITH ITS ORIGINAL INSTANCE ATTRIBUTES

#         self.color = color
#         self.bark_volume = bark_volume

#     def describe_self(self):
#         print(f"Hello there my name is {self.name}, i am {self.age} years old, i am {self.height}ft tall. and i am a {self.genus}")

# class Cat(Animal):
#     type = "cat"
#     genus = "feline"

#     def describe_self(self):
#         print(f"Hello there my name is {self.name}, i am {self.age} years old, i am {self.height}ft tall. and i am a {self.genus}")
    

# dog1 = Dog("Busky", 3, 3.6, "black", 10)
# dog2 = Dog("grumpy", 4, 4.6, "brown", 5)
# cat1 = Cat("slikee", 2, 2.4)

# # dog1.talk()
# # cat1.talk()
# print(dog1.genus)
# print(cat1.genus)
# # print(animal1.genus) # ANIMAL NEVER HAD THE ABILITY TO DECRIBE A GENUS ONLY IN THE CHILDREN WHO HAVE INHERITED FROM HER CAN SAID ATTRIBUTE BE ACCESSED. 
# dog1.describe_self()

# ##  A SET OF CLASSES THAT ACT LIKE A USER'S NOTEPAD BUT CAN ONLY WRITE

# class User():

#     def __init__(self, name):
#         self.name = name

# class Notepad:
    
#     def __init__(self, user):

#         self.body = ""
#         self.title = ""
#         self.user = user

#     def create_note(self):

#         title = input("Please enter your note title : ")
#         body = input("Please enter your note body : ")
#         username = self.user.name

#         note = f"{title},{body},{username}\n"

#         self.store_note(note)

#     def store_note(self, note):

#         file = open("notes.csv", "a")

#         file.write(note)
#         file.close()

# name = input("Please enter your name : ")
# me = User(name= name)

# my_notepad = Notepad(me)

# my_notepad.create_note()


#  A SET OF CLASSES THAT ACT LIKE A USER'S NOTEPAD AND ALLOW FOR READ AND WRITE

class User():

    def __init__(self, name):
        self.name = name

class Notepad:
    
    def __init__(self, user):

        self.body = ""
        self.title = ""
        self.user = user

    def create_note(self):

        title = input("Please enter your note title : ")
        body = input("Please enter your note body : ")
        username = self.user.name

        note = f"{title},{body},{username}\n"

        self.store_note(note)

    def store_note(self, note):

        file = open("notes.csv", "a")

        file.write(note)
        file.close()

    # THIS FUNCTION ALLOWS YOU TO READ ALL NOTES
    def read_notes(self):

        file = open("notes.csv")

        data = file.read()
        
        print(f"name".center(8), f"title".center(21), f"body".center(16), sep= " | ")
        print(f"-"*80)
        for line in data.splitlines():
            
            # print("-"*40)
            # print(line)
            # print()
            individual_components = line.split(",")
            #print(individual_components)

            title, body, name  = individual_components

            print(f"{name}".center(8), f"{title}".center(21), f"{body}".center(16), sep= " | ")
    
    # THIS FUNCTION ALLOWS YOU TO READ ONLY ONE PERSON'S NOTES
    
    def read_personal_notes(self):

        file = open("notes.csv")

        data = file.read()
        
        print(f"name".center(8), f"title".center(21), f"body".center(16), sep= " | ")
        print(f"-"*60)
        for line in data.splitlines():
            
            individual_components = line.split(",")

            title, body, name  = individual_components

            if name == self.user.name:

                print(f"{name}".center(8), f"{title}".center(21), f"{body}".center(16), sep= " | ")

        

            

name = input("Please enter your name : ")
me = User(name= name)

my_notepad = Notepad(me)

#my_notepad.create_note()
#my_notepad.read_personal_notes()
my_notepad.read_notes()

#count, mean, max, min, variance, most occuring


# class Data_Analyzer:

#     def __init__(self, filename):

#         self.filename = filename
#         self.numbers = []
#         self.read_file()

#     def read_file(self):

#         file = open(self.filename, "r")
#         data = file.read()

#         # print(data)
#         for number in data.splitlines():

#             int_version_of_number = int(number)

#             self.numbers.append((int_version_of_number))

#     def count(self):
#         # print(len(self.numbers))
#         return len(self.numbers)

#     def mean(self):
#         # print(sum(self.numbers)/len(self.numbers))
#         return sum(self.numbers)/self.count()
    
#     def max(self):
#         # print(max(self.numbers))
#         return max(self.numbers)
    
#     def min(self):
#         # print(min(self.numbers))
#         return min(self.numbers)

#     def variance(self):

#         x_minus_xbar = []
#         xbar = self.mean()

#         for x in self.numbers:

#             x_minus_xbar.append((x - xbar)**2)
        
#         summation_x_xbar = sum(x_minus_xbar)

#         squared_variance = summation_x_xbar/self.count() - 1
#         variance = squared_variance ** 0.5
#         print(variance)
        

            

# analyzer = Data_Analyzer("numbers.csv")
# print(analyzer.numbers)
# print(analyzer.count())
# print(analyzer.mean())
# print(analyzer.max())
# print(analyzer.min())

# analyzer.variance()