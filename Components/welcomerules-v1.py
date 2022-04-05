import random
from random import randint

from time import sleep 

# list of names working in business
names = ["Andy","Hunter","Joyce","Mengying","Pup","Bandi","Yuki","Niko",]

def welcome():
    """
    Purpose: to generate a random name for the list and and print out
    a welcome message.
    Parameters: none
    Returns: none
    """
num = randint(0,7)
name = (names[num])
# printing welcome message and rules
print("** Hello! Welcome to Nikoco's Commissions! My name is",name,"**")
print("** I will be helping you to create your art commission. ^^ **")
print("")
print("There are conditions as to what the artist can and cannot draw for you:")
print(" - Cannot draw mecha (heavily detailed pieces) \n - Cannot draw surrealistic/unrealistic portraits \n - Cannot draw anything depictive of offensive or hateful content")
print(" - One order maximum for one user regardless of work size")
print(" Orders that break the following conditions will be cancelled.")
print("")

def y_or_n():
    inp = input("Do you agree to these terms? (Y/N). ").lower()
    if inp == "y":
# inputs 'y' as agreeing to terms
        print("yas")
    elif inp == "n":
# inputs 'n' as disagreeing to terms
        print("** I'm sorry, you must agree to these terms in order to commission the artist. **")
        print("** If you wish to restart the program, type 1 ")
        print("** If you wish to exit the program, type 2 ")
        print("")

    else:
        print("Please enter either 'y' or 'n'")
        return y_or_n()
y_or_n()
