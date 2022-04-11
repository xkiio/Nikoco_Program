# Nikoco commissions program
# Bugs - phone number input allows letters
#      - name input allows numbers

# allows program to process a randomized output - for name randomization
import random
from random import randint

# list of names working in business
names = ["Andy","Hunter","Joyce","Mengying","Pup","Bandi","Yuki","Niko",]

# list of virtual options
virtual_options = ['Landscape Layout','Portrait (Full body)','Portrait (Half body)','Square Canvas/Album Cover','Wallpaper- Laptop/Tablet','Wallpaper- Iphone','Character Design Ref','Profile Picture',]
# list of physical options
physical_options = ['Landscape Layout','Poster Style','Portrait (Full body)','Portrait (Half body)','Square Canvas/Album Cover','Character Design Collage','Iphone Case','Sticker Designs (x5)',]

# list of virtual option prices
virtual_prices = [150, 100, 80, 60, 50, 50, 30, 10]
# list of physical option prices
physical_prices = [150, 130, 100, 80, 60, 35, 15, 10]

#list to store ordered pizzas
order_list = []
# list to store pizzas prices
order_cost = []
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
    y_or_n()

# yes or no condition funtion input
def y_or_n():
    while True:
        try:
            inp = input("Do you agree to these terms? (Y/N). ").lower() # asks for input automatically set to lower case.
            if inp == "y": # if input entered is y print following message
            # inputs 'y' as agreeing to terms
                print("** Perfect! **")
                break #sends user to continue main function process
            elif inp == "n": # if input entered is n sends user to n function
                n()
            else: # if input is invalided that is not y or n prints error message and loops
                print("Please enter either 'y' for yes, or 'n' for no.")
        except ValueError:
            print("That is not a valid answer.")
            print("Please enter either 'y' for yes, or 'n' for no.")

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
    p_v = ""
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
                    print ("** For a virtual delivery, we would like your name, phone number, and email address where the final product will be sent! **")
                    print ("** It is important that your details are correct- if you have made a mistake, you can reset your details after full input. **")
                    virtual_info()
                    p_v = "virtual"
                    break
                elif virtual == 2: # if input is 2 follows physical order function
                    print ("")
                    print ("** For a physical delivery, we would like your name, phone number and home address where the final product will be sent! **")
                    print ("** It is important that your details are correct- if you have made a mistake, you can reset your details after full input. **")
                    physical_info()
                    p_v = "physical"
                    break
            else: # if input is invalid prints error message
                print ("The number must be either 1 or 2.")
        except ValueError: # if input is blank or an invalid character prints error message
            print ("That is not a valid number.")
            print ("Please enter either 1 or 2.")
    return p_v

# virtual_info function - name, phone number and email address
def virtual_info():
# basic instructions
    print ("** Please enter the following... **")
    question = ("Name: ") # asks for name
    customer_details['name'] = not_blank(question)
    #print(customer_details['name'])

    question = ("Phone number: ") # asks for phone number
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])

    question = ("Email address: ") # asks for email address
    customer_details['email'] = not_blank(question)
    #print(customer_details['email'])
    print("")

# physical_info function - house address and phone
def physical_info():
# basic instructions
    print ("** Please enter the following... **")
    question = ("Name: ") # asks for name
    customer_details['name'] = not_blank(question)
    #print(customer_details['name'])

    question = ("Phone number: ") # asks for phone number
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])

    question = ("House number: ") # asks for house number
    customer_details['house'] = not_blank(question)
    #print(customer_details['house'])
    
    question = ("Street name: ")
    customer_details['street'] = not_blank(question)
    #print(customer_details['street'])

    question = ("Suburb: ")
    customer_details['suburb'] = not_blank(question)
    #print(customer_details['suburb'])

    question = ("State/city: ")
    customer_details['region'] = not_blank(question)
    #print(customer_details['region'])

    question = ("Postcode: ")
    customer_details['postcode'] = not_blank(question)
    #print(customer_details['postcode'])
    print("")

def menu(p_v):
    if p_v == "virtual":
        menu_virtual()
    if p_v == "physical":
        menu_physical()

# nikoco commission menu - virtual
def menu_virtual():
    number_options = 8
    for count in range(number_options) :
        print("{} {} ${:.2f}" .format(count+1, virtual_options[count],virtual_prices[count]))
    print("")
    # ask if user wishes to create another order.
    print("** Do you also wish to make a second commission? **")
    print("** Making another commission will prolong the time the order takes to be delivered to you. **")
    print("** If you do not, enter 1. If you do, enter 2: **")
    num_ordered = 0

# choose option of one or two orders - min 1, max 2
    while True:
        try:
            num_ordered = int(input(""))
            if num_ordered >= 1 and num_ordered <= 2:
                break
            else:
                print("Im sorry, your amount of commissions is limited to 2.")
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter either 1 or 2:")

    # choose options from menu
    print ("** Enter your",num_ordered,"commission(s) by entering its following number from the menu: **")
    for item in range(num_ordered):
        if num_ordered > 0  :
            while True:
                try:
                    commissions_ordered = int(input(""))
                    if commissions_ordered >=1 and commissions_ordered <=8:
                        break
                    else:
                        print ("Your order must be chosen out of the 8 options- please enter a number between 1-8: ")
                except ValueError:
                    print ("That is not a valid number.")
                    print ("Please enter a number between 1-8.")
            commissions_ordered = commissions_ordered -1 #Count down until all pizzas are ordered
            order_list.append(virtual_options[commissions_ordered])
            order_cost.append(virtual_prices[commissions_ordered])
            print("{} ${:.2f}" .format(virtual_options[commissions_ordered],virtual_prices[commissions_ordered])) #Count down until all pizzas are ordered
            num_ordered = num_ordered - 1          

# nikoco commission menu - physical
def menu_physical():
    number_options = 8
    for count in range(number_options) :
        print("{} {} ${:.2f}" .format(count+1, physical_options[count],physical_prices[count]))
    print("")        
    # ask if user wishes to create another order.
    print("** Do you also wish to make a second commission? **")
    print("** Making another commission will prolong the time the order takes to be delivered to you. **")
    print("** If you do not, enter 1. If you do, enter 2: **")
    num_ordered = 0

# choose option of one or two orders - min 1, max 2
    while True:
        try:
            num_ordered = int(input(""))
            if num_ordered >= 1 and num_ordered <= 2:
                break
            else:
                print("Im sorry, your amount of commissions is only limited to 2.")
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter either 1 or 2:")

    # choose options from menu
    print ("** Enter your",num_ordered,"commission(s) by entering its following number from the menu: **")
    for item in range(num_ordered):
        if num_ordered > 0  :
            while True:
                try:
                    commissions_ordered = int(input(""))
                    if commissions_ordered >=1 and commissions_ordered <=8:
                        break
                    else:
                        print ("Your order must be chosen out of the 8 options- please enter a number between 1-8: ")
                except ValueError:
                    print ("That is not a valid number.")
                    print ("Please enter a number between 1-8.")
            commissions_ordered = commissions_ordered -1 #Count down until all pizzas are ordered
            order_list.append(physical_options[commissions_ordered])
            order_cost.append(physical_prices[commissions_ordered])
            print("{} ${:.2f}" .format(physical_options[commissions_ordered],physical_prices[commissions_ordered]))
            num_ordered = num_ordered - 1          

# print order out - including if order is del or pickup and names and price of each pizza - total cost including any delivery charge
def print_order(p_v):
    total_cost = sum(order_cost)
    print()
    print("----------------------------------")
    print("* Your Details")
    if p_v == "physical":
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}, {customer_details['region']} {customer_details['postcode']}")
        print("You are ordering a physical copy- \nadditional shipping fee of $7.00")
        total_cost = total_cost + 7
    elif p_v == "virtual":
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Email: {customer_details['email']}")
        print("You are ordering a virtual copy.")
    print()
    print("** Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}, ${:.2f}".format(item, order_cost[count]))
        count = count  +1
    print()
    print("*** Order Cost Details")
    print(f"Your total cost is ${total_cost:.2f}")
    print("----------------------------------")
    print()

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
    p_v = order_type()
    menu(p_v)
    print_order(p_v)

main()