
import math
# Test of oop
"""
values = {4:4, 8:8, "Q":10, "ACE":11}
card = ("Q", "Hearts")
print("{}".format(values[card[0]]))
"""

### CREATING AND INSTANTIATING A CLASS
class Car():
    pass

# creating an instance of the car class and storing it in a variable ford
ford = Car()
subaru = Car()
#print(hash(ford))# hash output the memory location of yhe variable
#print(hash(subaru))# hash output the memory location of yhe variable

"""
# Another class
class Animal():
    pass
 lion = Animal()
 tiger = Animal()
"""

 # Attributes of a class
class Car():
    sound = "beep"
    color = "red"

ford = Car()
subaru = Car()

#print(ford.sound)
#print(subaru.color)

# You can change an attribute of an instance of a class
ford.sound = "honk"
#print(ford.sound)
#print(subaru.sound)


# using the __init__() method
# Using the __init__ method to give instance personal attributes
class Car():
    def __init__(self, color):
        self.color = color

ford = Car("blue")
#print(ford.color)


# Instantiating multiple objects wit __init__
class Car():
    pie = math.pi # Global accessible attribute
    def __init__(self, color, year):
        self.color = color   # instance accessible attribute
        self.year = year

ford = Car("Red", 2016)
subaru = Car("blue", 2018)

#print(ford.pie)
#print(ford.color, ford.year)
#print(subaru.color, subaru.year)
#print(Car.pie) # Global attribute


## Exercises
"""
class Dogs():
    species = "Canine"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dogs("Sammi","Husky")
dog2 = Dogs("Casey","Chocolate Lab")

#print(dog1.name, dog1.breed)
#print(dog2.name, dog2.breed)


class Person():
    def __init__(self, name):
        self.name = name

n = input("Enter your name: ")
person1 = Person(n)
print("Your name is {}".format(person1.name))
"""


## Methods

class Dog():
    def makeSound(self):
        print("bark")

sam = Dog()
#sam.makeSound() # calling a method in a class

## ACCESSING CLASS ATTRIBUTES IN METHODS
# Using the self keyword to access attributes within class methods

class Dog():
    sound = "whow"
    def makeSound(self):
        print(self.sound) # self required to access attributes defined in the class

sam = Dog()
#sam.makeSound()



# Method Scope
# methods accessible by the class only but not instance of the class is called STATIC METHOD

#understanding which methods are accesible via the class itself and class instances
class Dog():
    sound = "bark"
    def makeSound(self):
        print(self.sound)

    def printInfo():
        print("I am a dog.")

#Dog.printInfo() # able to run printInfo method because it not include self parameter
#Dog.makeSound() would produce error, self is in reference to instances only

sam = Dog()
#sam.makeSound() # able to access, self can reference the  of sam
# sam.printInfo() will produce error, instances require the self parameter to access methods


##passing argument into methods

# writing methods that accept parameters
class Dog():
     def showAge(self, age):
         print(age) # does not need self, age is referencing the parameter not an attribute

sam = Dog()
#sam.showAge(6) # passing the integer 6 as an argument to the showAge method


## Methods Calling Methods

# calling a class method from another method
class Dog():
    age = 6
    def getAge(self):
        return self.age
    def printInfo(self):
        if self.getAge()< 10:
            print("Puppy!")

sam = Dog()
#sam.printInfo()


## Magic Methods
# magic methods usually comes with two underscores
# examples
# __str__

class Dog():
    def __str__(self):
        return "this is a dog class"

sam = Dog()
#print(sam) # will print the return of the string


## Exercises
class Animals():
    name = " "
    def setSpecies(self, species):
        self.name = species

    def getSpecies(self):
        return self.name


lion = Animals()
lion.setSpecies("feline")
#print(lion.getSpecies())


"""
class Person():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def setAge(self):
        age = input("Enter your age: ")
        self.age = age

    def getAge(self):
        return ("{} are {} years old.".format(self.name, self.age))


name = input("Enter your name: ")
person2 = Person(name)
person2.setAge()
print(person2.getAge())
"""

### Inheritance

# inheriting a class and accessing the inherited method
class Animal():
    def makeSound(self):
        print("roar")

class Dog(Animal): # inheriting Animal class
    species = "Canine"

sam = Dog()
#sam.makeSound() # accessible through inheritance

lion = Animal()
#lion.species not accessible, inheritance does not backwards


## super() method

# using the super() method to declare inherited attributes

class Animal():
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, species, name):
        self.name = name
        super().__init__(species) # using super to declare the species attribute defined in Animal

sam = Dog("Canine","Sammi")
#print(sam.species)

## Inheriting Multiple Classes

# how to inherit multiple classes
class Physics():
    gravity = 9.8

class Automobile():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Ford(Physics, Automobile): # able to access Physics and Automobile attributes and methods
    def __init__(self, model, year):
        Automobile.__init__(self,"Ford", model, year) # super does not work with multiple

truck = Ford("F-150", 2018)
#print(truck.gravity, truck.make) # it output both attribute


###  Exercise
class Character():
    def __init__(self, name, team, height, weight):
        self.name, self.team, self.height, self.weight = name, team, height, weight

    def sayHello(self):
        print("Hello, my name is {} and I'm on the {} guys".format(self.name, self.team))

class GoodPlayers(Character):
    def __init__(self, team="good"):
        self.team = team
        super().__init__(name,team, height, weight)


class BadPlayers(Character):
    def __init__(self, team="bad"):
        self.team = team
        super().__init__(name, team, height, weight) # self is not needed


name = input("Enter your name: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")

player1 = GoodPlayers()
#player1.sayHello()
player2 = BadPlayers()
player2.sayHello()