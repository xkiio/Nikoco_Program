# Nikoco commissions program
# Bugs - phone number input allows letters
#      - name input allows numbers

# allows program to process a randomized output - for name randomization
import random
from random import randint

# list of names working in business
names = ["Andy","Hunter","Joyce","Mengying","Pup","Bandi","Yuki","Niko",]

# customer details dictionary
customer_details = {}

# validates inputs to check if they are blank.
# takes question as a parameter
# returns response in title class if valid - capitalizes first letter of words' input
def not_blank(question):
    valid = False
    while not valid: # sets up while loop
        response = input(question) # asks for input(string)
        if response != "": # if input is valid prints response and continues other functions.
            return response.title()
        else: # if input is invalid prints error message
            print("This cannot be blank.")
            
# defining welcome page
def welcome():
    """
    Purpose: to generate a random name for the list and and print out
    a welcome message.
    Parameters: none
    Returns: none
    """
    num = randint(0,7) # randomized number from 0 to 7
    name = (names[num]) # assigns each given name with a number from 0 to 7
    # printing welcome message and rules
    print("")
    print("** Hello! Welcome to Nikoco's Commissions! My name is",name,"**")
    print("** I will be helping you to create your art commission. ^^ **")
    print("")
    print("There are conditions as to what the artist can and cannot draw for you:")
    print(" - Cannot draw mecha (heavily detailed pieces) \n - Cannot draw surrealistic/unrealistic portraits \n - Cannot draw anything depictive of offensive or hateful content")
    print(" - Twos orders maximum for one user regardless of work size")
    print(" Orders that break the following conditions will be refunded.")
    print("")

# yes or no condition funtion input
def y_or_n():
    inp = input("Do you agree to these terms? (Y/N). ").lower() # asks for input automatically set to lower case.
    if inp == "y": # if input entered is y print following message
# inputs 'y' as agreeing to terms
        print("** Perfect! **")
        order_type() # sends user to order_type function
    elif inp == "n": # if input entered is n sends user to n function
        n()
    else: # if input is invalided that is not y or n prints error message and loops
        print("Please enter either 'y' for yes, or 'n' for no.")
        y_or_n()

# n function if user inputs n for conditions
def n():
    print("")
    print("** I'm sorry, you must agree to these terms in order to commission the artist. **")
    print("** If you wish to restart the program, type 1 **")
    print("** If you wish to exit the program, type 2 **")
    print("")
    while True: # sets up while loop
        try: # catches and handles exception by allowing a reboot/abort option
            restart = int(input("Please enter a number: ")) # asks for input
            if restart >= 1 and restart <= 2: # defines two options a number that is either 1 or 2
                if restart == 1: # if input is 1 sends user to reboot
                    main()
                    break
                elif restart == 2: # if input is 2 aborts program and prints farewell message
                    print ("** Have a good day! **")
                    print ("")
                    quit()
            else: # if input is outside boundary that is lower than 1 or higher than 2 prints error message
                print ("The number must be 1 or 2. ")
        except ValueError: # if input is left blank or invalid character prints error message
            print ("That is not a valid number.")
            print ("Please enter either 1 or 2.")

# order_type function and printing instructions
def order_type():
    print("")
    print ("** Do you want your order to be of virtual or physical use? **")
    print ("** For a virtual copy, enter '1' **")
    print ("** For a physical copy, enter '2' **")
    while True: # sets up while loop
        try: # allows two options that is either 1 or 2
            virtual = int(input("Please enter a number: ")) # asks for input
            if virtual >= 1 and virtual <=2: # if input is equal to 1 or 2 
                if virtual == 1: # if input is 1 follows virtual order function
                    print ("")
                    print ("**For a virtual delivery, we would like your name, phone number, and email address where the final product will be sent! **")
                    virtual_info()
                    break
                elif virtual == 2: # if input is 2 follows physical order function
                    print ("Physical")
                    break
            else: # if input is invalid prints error message
                print ("The number must be either 1 or 2.")
        except ValueError: # if input is blank or an invalid character prints error message
            print ("That is not a valid number.")
            print ("Please enter either 1 or 2.")

# virtual_info function - name, phone number and email address
def virtual_info():
# Basic instructions
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your email address: ")
    customer_details['email'] = not_blank(question)
    print(customer_details['email'])

# physical_info function - house address and phone


# nikoco commission menu


# choose option of one or two orders - min 1, max 2


# commission order - from menu - print options over


# print order out - including if order is del or pickup and names and price of each pizza - total cost including any delivery charge


# ability to cancel or proceed with order


# option for new order only if cancelled or exit


# main function
def main():
    """
    Purpose: to run all functions.
    Parameters: none
    Returns: none
    """
    welcome()
    y_or_n()

main()