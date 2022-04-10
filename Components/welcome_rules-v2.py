import random
from random import randint

# list of names working in business
names = ["Andy","Hunter","Joyce","Mengying","Pup","Bandi","Yuki","Niko",]

# defining welcome page
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
    print(" - Twos orders maximum for one user regardless of work size")
    print(" Orders that break the following conditions will be cancelled.")
    print("")

def y_or_n():
    inp = input("Do you agree to these terms? (Y/N). ").lower()
    if inp == "y":
# inputs 'y' as agreeing to terms
        print("** Perfect! **")
    elif inp == "n":
# inputs 'n' as disagreeing to terms
        print("** I'm sorry, you must agree to these terms in order to commission the artist. **")
        print("** If you wish to restart the program, type 1 **")
        print("** If you wish to exit the program, type 2 **")
        print("")
    else:
        print("Please enter either 'y' for yes, or 'n' for no.")
        return y_or_n()
    while True:
        try:
            restart = int(input("Please enter a number: "))
            if restart >= 1 and restart <= 2:
                if restart == 1:
                    main()
                    break
                elif restart == 2:
                    print ("** Have a good day! **")
                    print ("")
                    quit()
            else:
                print("The number must be 1 or 2. ")
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter 1 or 2.")

def main():
    """
    Purpose: to run all functions.
    Parameters: none
    Returns: none
    """
    welcome()
    y_or_n()

main()