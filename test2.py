# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:39:37 2020

@author: user
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#import math

#print(math.ceil(3.67)) #- print out the nearest integer  4
#print(math.floor(3.67)) # print out the integer 3


"""
radius = 6371.01
x1 = math.radians(float(input("Enter the latitude for point 1: ")))
y1 = math.radians(float(input("Enter the longitude for point 1: ")))
x2 = math.radians(float(input("Enter the latitude for point 2: ")))
y2 = math.radians(float(input("Enter the longitude for point 2: ")))
d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("The distance between the two points is ", d, "km")
"""

"""
n = 7
#for i in range(n):
    #print(i*"x")
    
from time import time, ctime
    
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

    # THIS FUNCTION ALLOWS YOU TO READ ALL NOTES
    def read_notes(self):

        file = open("notes.csv")

        data = file.read()
        
        print(f"name".center(8), f"title".center(21), f"body".center(16), f"time".center(25), sep= " | ")
        print(f"-"*80)
        for line in data.splitlines():
            
            # print("-"*40)
            # print(line)
            # print()
            individual_components = line.split(",")
            # print(individual_components)

            title, body, name, time = individual_components

            print(f"{name}".center(8), f"{title}".center(21), f"{body}".center(16), f"{time}".center(25), sep= " | ")
            
#me = User("Dele")
#new = Notepad(me)
#new.create_note()


#print(new.read_notes())


#print(f"name".center(8), f"title".center(21), f"body".center(16), f"time".center(10), sep= " | ")
#print(f"-"*80)
  
"""          

"""
def createNote():
    n=input("Enter name: ")
    ti=input("Enter title: ")
    b=input("enter message: ")
    t = ctime(time())
    note = f"{ti},{b},{n},{t}\n"
    file = open("new.csv","a")
    return file.write(note)

#print(createNote())
def read(fn):
    file = open("new.csv")
    data = file.read()
    for line in data.splitlines():
        ind_c = line.split(",")
        title, body, name, time = ind_c
        print(f"{name}".center(8), f"{title}".center(21), f"{body}".center(16), f"{time}".center(25), sep= " | ")

#createNote()
#createNote()
#read(createNote()) 
        
x = [i for i in range(1, 15, 2)]
print(x.mean())


"""
"""
class User():
    client = {"Essien":23456, "James":65432}
    pwd = {"Essien":2323, "James":4545}
    
    def __init__(self, name, password, amount= 0):
        self.name = name
        self.password = password
        self.amount = amount
        
    def check_balance(self):
        print("Your account balance is {:.2f}".format(User.client[self.name]))
        
    def sign_up(self, person):
        person.pwd[self.name] = self.password
        person.client[self.name] = self.amount
        print("Congratulation for signing up!")
        
    def log_out(self):
        exit()

    def sign_in(self, person):
        if self.name in person.pwd.keys() | self.password in person.pwd.values():
            print("Welcome to bank ABC")
            self.check_balance()
        else:
            print("Your name or password does not exist\n Sign up")
            status = int(input("Enter 1 to sign-up or 0 to log-out: "))
            if status == 1:
                self.sign_up(person)
            else:
                self.log_out()
                
    
              
              
print("Sign in with your name and password")              
name = input("Enter name: ")
password = input("Enter password: ")

user = User(name, password)
user1 = User(name, password)


#user1.check_balance()
#user1.sign_in(user)
#print(user.client)
print(user.pwd)
"""
"""

data1 = np.random.randint(1, 100, 100)
data2 = np.random.randint(1, 100, 100)


plt.scatter(x=data1, y=data2, c=(data1+data2)/2, cmap="magma")
plt.colorbar(label="third data")
"""



from array import *

import seaborn as sns
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#mport numpy as np

"""
df = sns.load_dataset("tips")
print(df.head())
print("*"*50)
groupedvalues=df.groupby('day').mean().reset_index()

pal = sns.color_palette("Greens_d", len(groupedvalues))
rank = groupedvalues["tip"].argsort().argsort() 
g=sns.barplot(x='day',y='tip',data=groupedvalues, palette=np.array(pal[::-1])[rank])

for index, row in groupedvalues.iterrows():
    g.text(row.name,row.tip, round(row.tip,2), color='red', ha="center")

plt.show()


plt.figure(figsize=(8, 6))
splot=sns.barplot(x="continent",y="lifeExp",data=df)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
plt.xlabel("Continent", size=14)
plt.ylabel("LifeExp", size=14)
plt.savefig("add_text_to_top_of_bars_in_barplot_Seaborn_Python.png")
"""
#input1 =   array("i",[5,"\n",23,"",34,"\n",45, "",56,"\n",67]).tolist()

#print(input1)

#print(2**5 - 1)
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def get_primes(n_start, n_end):
    mersenne = []
    for number in range(n_start, n_end):
        if is_prime(number):
            mersenne.append(number)
    return mersenne

ls = get_primes(3,65)
#print(ls)

def mersenne_number(p):
    mersenne_ = []
    for item in p:
        mersenne_.append(2**item - 1)
    return mersenne_

#print(mersenne_number(ls))






n0=4
n0=4
 
#ni=(n2i−1−2)mod(2p−1)
#def recus(n):
#    if 


def lucas_lehmer(p):
    ls=[]
    n0=(4**2-2)%(2**p - 1)
    ls.append(n0)
    for item in range(1, p):
        if item <= p-2:
            ls.append(((item-1)**2-2)%(2**p - 1))
    return sorted(ls)

#print(lucas_lehmer(17))
    


ls = [['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?'], 'casino']
item = "Casino"

item = item.lower()
ls2 = []

for i in ls:
    ls2.append(i)



import math
import numpy as np

a = -0.5 * np.log2(0.5)-0.5*np.log2(0.5)
#print(a)


def digits(n):
	count = 0
	if n == 0:
	  count = 1
	while n > 0:
		count += 1
		n = n//10
	return count
	
#print(digits(25))   # Should print 2
#print(digits(144))  # Should print 3
#print(digits(1000)) # Should print 4
#print(digits(0))    # Should print 1
    

def multiplication_table(start, stop):
    for x in range(start, stop+1):  
        for y in range(1, stop+1):
            print(str(x*y), end=" ")
        #print()

#multiplication_table(1, 3)
# Should print the multiplication table shown above

#multiplication_table(1, 12)

strf = "string function"
#print(strf[::-1])



def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for a in range(0,(len(input_string)-1)//2):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if input_string[a] != " ":
			new_string = input_string[a]            
			reverse_string = input_string[-a-1]
    #print(new_string)
	# Compare the strings
	if new_string.lower() == reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be Tru



python
