import math
import random
import numpy as np


name = input("Enter a username ")
if name != np.nan:
    #print("\n")
    print("Your are welcome ", name)
    print("The game has five levels ranging from simple to advance arithmetic questions. \n The first level has five questions")
    print("LEVEL 1 (SIMPLE) \n")
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 5)
    print("Question 1. \n What is "+ str(n1)+" + "+str(n2)+" ? ")
    ans1 = eval(input("Answer "))

    if ans1 == n1+n2:
        print("Correct \n The answer is", n1+n2)
        print("\n Question 2.\n")
        n3 = random.randint(1, 10)
        n4 = random.randint(1, 5)
        print("What is "+ str(n3)+" x "+str(n4)+" ? ")
        ans2 = eval(input("Answer "))

        if ans2 == n3*n4:
            print("Correct \n The answer is", n3*n4)
            print("\n Question 3.\n")
            n5 = random.randint(1, 10)
            n6 = random.randint(1, 5)
            print("What is the product of ("+ str(n5)+" and "+str(n6)+") raise to 2? ")
            ans3 = eval(input("Answer "))

            if ans3 == (n5*n6)**2:
                print("Correct \n The answer is", (n5*n6)**2)
                print("\n Question 4. \n")
                n7 = random.randint(1, 10)
                n8 = random.randint(1, 5)
                print("What is "+ str(n7)+" - "+str(n8)+" ? ")
                ans4 = eval(input("Answer "))

                if ans4 == n7-n8:
                    print("Correct \n The answer is", n7-n8)
                    print("\n Question 5. \n")
                    n9 = random.randint(1, 10)
                    n10 = random.randint(1, 5)
                    print("What is ("+ str(n9)+" - "+str(n10)+") x ("+str(n9)+" + "+str(n10)+") ?")
                    ans5 = eval(input("Answer "))
                    if ans5 == (n9-n10)*(n9+n10):
                        print("Correct \n The answer is", (n9-n10)*(n9+n10))
                        print("Congratulation "+ name+"\n \n\t\t\t\t Level 2")

                    else:
                        print("Wrong \n The answer is", (n9-n10)*(n9+n10))
                        print("Congratulation for getting to this stage ")

                else:
                    print("Wrong \n The answer is", n7-n8)

            else:
                print("Wrong \n The answer is", (n5*n6)**2)

        else:
            print("Wrong \n The answer is", n3*n4)
            
    else:
        print("Wrong \n The answer is", n1+n2)