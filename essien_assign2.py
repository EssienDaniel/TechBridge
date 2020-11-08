
import math
import random

# Ex. 4.1
"""
a = eval(input("Enter a value for a "))
b = eval(input("Enter a value for b "))
c = eval(input("Enter a value for c "))

d = b**2 - 4*a*c
#r1 = (-b + math.sqrt(d))/2*a
#r2 = (-b - math.sqrt(d))/2*a
#r1 = round(r1, 5)
#r2 = round(r2, 5)

if d > 0:
    r1 = (-b + math.sqrt(d))/2*a
    r2 = (-b - math.sqrt(d))/2*a
    r1 = round(r1, 5)
    r2 = round(r2, 5)
    print("The roots are", r1,"and",r2)
elif d==0:
    r1 = (-b + math.sqrt(d))/2*a
    r1 = round(r1, 5)
    print("The root is", r1)
else:
    print("The equation has no real roots")
"""


# EX. 4.4
"""
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
answer = eval(input("What is "+ str(num1) + " + "+ str(num2) + "? "))
if answer == num1 + num2:
    print(str(answer==num1+num2) + "\n" + str(num1) + " + "+ str(num2) + " = " + str(num1+num2))
else:
    print(str(answer==num1+num2) + "\n" + str(num1) + " + "+ str(num2) + " = " + str(num1+num2))

"""

# EX. 4.17

"""
player = eval(input("scissor(0), "+" rock(1), "+" paper(2): "))
computer = random.randint(0, 2)
if computer==0 and player == 0:
    print("The computer is scissor. You are scissor too. It is a draw.")
elif computer==0 and player == 1:
    print("The computer is scissor. You are rock. You won.")
elif computer==0 and player ==2:
    print("The computer is scissor. You are paper. Computer won.")
elif computer==1 and player==0:
    print("The computer is rock. You are scissor. Computer won")
elif computer==1 and player==1:
    print("The computer is rock. You are rock too. It is a draw.")
elif computer==1 and player==2:
    print("The computer is rock. You are paper. You won.")
elif computer==2 and player==0:
    print("The computer is paper. You are scissor. You won.")
elif computer==2 and player==1:
    print("The computer is paper. You are rock. Computer won.")
elif computer==2 and player==2:
    print("The computer is paper. You are paper too. It is a draw.")
else:
    print("Invalid entry")

"""

# EX. 4.21
year = eval(input("Enter year: (e.g., 2008): "))
m = eval(input("Enter month: 1-12: "))
q = eval(input("Enter the day of the month: 1-31: "))
j = year/100
k = year % 100

h = (q + math.floor(26*(m + 1)/10) + k + math.floor(k/4) + math.floor(j/4) + 5*j) % 7

if h==0:
    print("Day of the week is Saturday")
elif h==1:
    print("Day of the week is Sunday")
elif h==2:
    print("Day of the week is Monday")
elif h==3:
    print("Day of the week is Tuesday")
elif h==4:
    print("Day of the week is Wednesday")
elif h==5:
    print("Day of the week is Thursday")
elif h==6:
    print("Day of the week is Friday")
else:
    print("One or more of the entries are invalid")