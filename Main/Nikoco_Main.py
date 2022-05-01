# Nikoco Commissions program
# Bugs - phone number input allows letters
#      - name input allows numbers

# Known bugs
# 30/04/22 - Customer details allows any input without an '@' and '.'

# importing function class into program - for use of quitting system
import sys
# allows program to process a randomized output - for name randomization
import random
from random import randint

# importing regular expressions - for use of specifying a string that matches
import re

# constants
# general low and high limit
LOW = 1
HIGH = 2
# low and high limit for phone number input
PH_LOW = 7
PH_HIGH = 15
# low and high limit for house number input
HOUSE_LOW = 1
HOUSE_HIGH = 6
# low and high limit for postcode limit
POST_LOW = 4
POST_HIGH = 10

# list of names working in business
names = ["Andy", "Hunter", "Joyce", "Mengying", "Pup", "Bandi", "Yuki", "Niko"]

# list of virtual options
virtual_options = ['Landscape Layout', 'Portrait (Full body)',
                   'Portrait (Half body)', 'Square Canvas/Album Cover',
                   'Wallpaper- Laptop/Tablet', 'Wallpaper- Iphone',
                   'Character Design Ref', 'Profile Picture']
# list of physical options
physical_options = ['Landscape Layout', 'Poster Style',
                    'Portrait (Full body)', 'Portrait (Half body)',
                    'Square Canvas/Album Cover',
                    'Character Design Collage', 'Iphone Case',
                    'Sticker Designs (x5)']

# list of virtual option prices
virtual_prices = [150, 100, 80, 60, 50, 50, 30, 10]
# list of physical option prices
physical_prices = [150, 130, 100, 80, 60, 35, 15, 10]

# list to store ordered pizzas
order_list = []
# list to store pizzas prices
order_cost = []
# customer details dictionary
customer_details = {}


# validates inputs to check if they are blank or not.
# takes question as a parameter
# returns response in title class if valid
def not_blank(question):
    # initial meaning of valid (FALSE) unless given otherwise
    valid = False
    # sets up while loop
    while not valid:
        # asks for input(string)
        response = input(question)
        # if an input is typed prints response and continues other functions.
        if response != "":
            # - capitalizes first letter of words' input
            # sends response back to initial variable
            return response.title()
        # if response is not given any input
        else:
            # if input is invalid prints error message
            print("This cannot be blank.")


# validates inputs to check if they are a string
# takes question as a parameter
def check_string(question):
    # sets up while loop
    while True:
        # asks for input(string)
        response = input(question)
        # checks that input is in aphabetical and sets x to True if alpha
        x = response.isalpha()
        # if x is False prints error message
        if not x:
            print("Input must only contain letters.")
        # if x is True will return response
        else:
            # returns response in title class if valid
            return response.title()


# validates inputs to check if they are an integer.
# takes question, low and high as a parameter
def val_int(low, high, question):
    # sets up while loop
    while True:
        # tests following blocks of code for errors
        try:
            # asks for an integer only input
            num = int(input(question))
            # allows two options that is either 1 or 2
            if num >= low and num <= high:
                # if input is equal to 1 or 2
                # will return integer to title class
                return num
            # if input given is not 1 or 2- prints error message
            else:
                print ("Please enter a number that is either", low, "or", high)
        # if input is exceptional to invalid input of integers-
        # eg. blanks, foreign characters
        except ValueError:
            # prints error message
            print ("That is not a valid number.")
            print ("Please enter a number that is either", low, "or", high)


# validates inputs to check that the integers are in
# range of what the program asks
# takes question, PH_LOW, and PH_HIGH as a parameter
def check_int(question, PH_LOW, PH_HIGH):
    # sets up while loop
    while True:
        # tests following blocks of code for errors
        try:
            # asks for an integer only input
            num = int(input(question))
            # using input number as its number
            test_num = num
            # initial count is 0 until count input is stored
            count = 0
            # while the input number is greater than 0
            while test_num > 0:
                # input number is divided by ten to count how
                # many digits there are, the phone can then
                # be validated after interpreting if number
                # of digits are ranged between PH_LOW and PH_HIGH
                test_num = test_num//10
                # count added to start with 1
                count = count + 1
            # if the count is equal to phone number range,
            # will send result input back to caller.
            if count >= PH_LOW and count <= PH_HIGH:
                return str(num)
            # if integer input is invalid
            # prints error message
            else:
                # only when asked for house number
                if PH_LOW == HOUSE_LOW and PH_HIGH == HOUSE_HIGH:
                    print("House numbers are limited between", HOUSE_LOW,
                          "and", HOUSE_HIGH, "digits.")
                # only when asked for postcode
                elif PH_LOW == POST_LOW and PH_HIGH == POST_HIGH:
                    print("Postcodes are limited between", POST_LOW,
                          "and", POST_HIGH, "digits.")
                # only when asked for phone number
                elif PH_LOW == PH_LOW and PH_HIGH == PH_HIGH:
                    print("Phone numbers are limited between", PH_LOW,
                          "and", PH_HIGH, "digits.")
        # if input was a foreign character exclusive to integers
        # prints error message
        except ValueError:
            # only when asked for house number
            if PH_LOW == HOUSE_LOW and PH_HIGH == HOUSE_HIGH:
                print("Please enter your house number.")
            # only when asked for postcode
            elif PH_LOW == POST_LOW and PH_HIGH == POST_HIGH:
                print("Please enter your postcode- "
                      "hyphens and spaces are not necessary.")
            # only when asked for phone number
            elif PH_LOW == PH_LOW and PH_HIGH == PH_HIGH:
                print("Please enter your phone number- "
                      "hyphens and spaces are not necessary.")


# validates the email input to check that its format is correct.
# takes question as a parameter
def valid_email(question):
    # sets up while loop
    while True:
        # asks for input(string)
        require = input(question)
        # setting requirement for validating email input
        # must include an '@' and '.' as well as
        # a 3 character limit after these symbols
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        # breaks out of def function if input meets pat requirements
        # takes pat and require as a parameter
        if re.match(pat, require):
            break
        # if input does not match prints error message
        else:
            print("Please make sure that your email is correct, "
                  "and has inlcuded an '@' and a '.'")


# exit function for exiting the program
def exit():
        # prints farewell message
        print ()
        print ("** Thank you for using our Nikoco Commissions "
               "Program! We hope to see you again! **")
        print ()
        # clears any previous data in arrays and dictionary stored by the user.
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        # exits program.
        sys.exit()


# defining welcome page
def welcome():
    """
    Purpose: to generate a random name for the list and and print out
    a welcome message.
    Parameters: none
    Returns: none
    """
    # integer is randomized ranging from 0 to 7
    num = randint(0, 7)
    # assigns each given name with a random number from 0 to 7
    name = (names[num])
    # printing welcome message and rules
    print("")
    print("** Hello! Welcome to Nikoco's Commissions! My name is", name, "**")
    print("** I will be helping you to create your very "
          "own art commission. **")
    print("")
    print("There are conditions as to what the artist can and cannot "
          "draw for you:")
    print(" - Cannot draw mecha (heavily detailed pieces) \n"
          " - Cannot draw surrealistic/unrealistic portraits \n"
          " - Cannot draw anything depictive of offensive or "
          "hateful content")
    print(" - Twos orders maximum under one user's name regardless "
          "of work size")
    print("** Orders that break the following conditions will be "
          "refunded. **")
    print("")
    # continues program to y_or_n function
    y_or_n()


# yes or no condition function -
# used as a user confirmation if they have read the welcome page
def y_or_n():
    # sets up while loop
    while True:
        try:
            # asks for input(string) set to lower case
            # in case user enters capital letter of 'y' or 'n'
            inp = input("Do you agree to these terms? (Y/N). ").lower()
            # asks for input automatically set to lower case.
            if inp == "y":
                # if input entered is y print following message
                # inputs 'y' as agreeing to terms
                print("** Perfect! **")
                break
            # sends user to continue main function process
            elif inp == "n":
                # if input entered is n sends user to n function
                n()
            else:
                # if input is invalid that is not y or n
                # prints error message and loops
                print("Please enter either 'y' for yes, or 'n' for no.")
        except ValueError:
            # if input is invalid that is a foreign character or
            # space prints error message and loops
            print("That is not a valid answer.")
            print("Please enter either 'y' for yes, or 'n' for no.")


# n function if user inputs n for y_or_n function
def n():
    # asks for input(string) - indentifies question variable
    question = ("")
    # prints instructions whether user wishes to restart or exit
    print("")
    print("** I'm sorry, you must agree to these terms "
          "in order to commission the artist. **")
    print("** If you wish to restart the program, type 1 **")
    print("** If you wish to exit the program, type 2 **")
    # restart variable uses val_int function to
    # validate input and identify out of bound inputs
    restart = val_int(LOW, HIGH, question)
    # asks for input
    if restart == 1:
        # if input is 1 sends user to reboot
        print ()
        print ("Restarting program...")
        main()
    else:
        # if input is 2 aborts program
        # prints farewell message from exit function
        exit()


# order_type function and printing instructions
# - user choosing either virtual or physical copy
def order_type():
    # identifying p_v and question parameter
    p_v = ""
    question = ("")
    # prints instructions
    print("")
    print ("** Do you want your order to be of virtual or physical use? **")
    print ("** For a virtual copy, enter '1' **")
    print ("** For a physical copy, enter '2' **")
    # virtual variable using val_int function for catching input errors
    virtual = val_int(LOW, HIGH, question)
    # asks for input
    # if input is 1 follows virtual order function
    if virtual == 1:
        # prints virtual delivery instructions
        print ("")
        print ("** For a virtual delivery, we would like your name, "
               "phone number, and email address where the final "
               "product will be sent! **")
        print ("** It is important that your details are correct- "
               "if you have made a mistake, you can reset your "
               "details after full input. **")
        # stores p_v parameter as virtual
        p_v = "virtual"
        # sends program to virtual_info function for details
        virtual_info()
    # if input is 2 follows physical order function (NOT virtual function)
    else:
        # prints physical delivery instructions
        print ("")
        print ("** For a physical delivery, we would like your "
               "name, phone number "
               "and home address where the final product will be sent! **")
        print ("** It is important that your details are correct- if you have"
               " made a mistake, you can redo your details after "
               "a full input. **")
        # stores p_v parameter as physical
        p_v = "physical"
        # sends program to physical_info function for details
        physical_info()
    # returns parameter's result back whether physical or virtual
    return p_v


# virtual_info function - name, phone number and email address
# inputting customer details
def virtual_info():
    # basic instructions
    print ("** Please enter the following... **")
    # asks for name
    question = ("Name: ")
    # stores customer_details name with check_string function
    customer_details['name'] = check_string(question)

    # asks for phone number
    question = ("Phone number: ")
    # stores customer_details phone number with check_int function
    customer_details['phone'] = check_int(question, PH_LOW, PH_HIGH)

    # asks for email address
    question = ("Email address: ")
    # stores customer_details email with valid_email function
    customer_details['email'] = valid_email(question)
    # prints a newline
    print()


# physical_info function - house address and phone
# inputting customer details
def physical_info():
    # basic instructions
    print ("** Please enter the following... **")
    # asks for name
    question = ("Name: ")
    # stores customer_details name with check_string function
    customer_details['name'] = check_string(question)

    # asks for phone number
    question = ("Phone number: ")
    # stores customer_details phone number with check_int function
    customer_details['phone'] = check_int(question, PH_LOW, PH_HIGH)

    # asks for house number
    question = ("House number: ")
    # stores customer_details house number with check_int function
    customer_details['house'] = check_int(question, HOUSE_LOW, HOUSE_HIGH)

    # asks for street name
    question = ("Street name: ")
    # stores customer_details street name with check_string function
    customer_details['street'] = check_string(question)

    # asks for suburb name
    question = ("Suburb: ")
    # stores customer_details suburb name with check_string function
    customer_details['suburb'] = check_string(question)

    # asks for state/city name
    question = ("State/city: ")
    # stores customer_details state/city name with check_string function
    customer_details['region'] = check_string(question)

    # asks for postcode
    question = ("Postcode: ")
    # stores customer_details postcode with check_int function
    customer_details['postcode'] = check_int(question, POST_LOW, POST_HIGH)
    # prints a newline
    print()


# function which confirms or denies data input
# from virtual_info or physical_info
# takes p_v as a parameter
def detail_confirm(p_v):
    # identifying question parameter
    question = ("")
    # prints instructions- 1 or 2
    print ("** Please confirm your details... **")
    print ("To confirm, please enter '1' ")
    print ("To try again, please enter '2' ")
    # creating detail variable using val_int function for catching error inputs
    detail = val_int(LOW, HIGH, question)
    # if input detail is 1 prints confirmation message
    if detail == 1:
        print ("Details Confirmed.")
    # if input detail is 2 prints cancelled message
    else:
        print ("Details Cancelled.")
        print ()
        # if user chose virtual from order_type function
        # clears previous customer_details
        # sends user to redo virtual_info and detail_confirm function
        if p_v == "virtual":
            customer_details.clear
            virtual_info()
            # repeated until user confirms customer details
            detail_confirm(p_v)

        # if user chose virtual from order_type function
        # clears previous customer_details
        # sends user to redo physical_info and detail_confirm function
        else:
            customer_details.clear
            physical_info()
            # repeated until user confirms customer details
            detail_confirm(p_v)


# prints menu for chosen option (virtual or physical)
# takes p_v as a parameter
def menu(p_v):
    # identifying number of menu options
    number_options = 8
    # if user chose virtual from order_type function prints virtual menu
    if p_v == "virtual":
        print()
        # generates a series of numbers in the range of number_options
        for count in range(number_options):
            # formats menu for menu list to be ranged 1-8 options (not 0-8)
            # dollar sign added before menu
            # option prices and include price decimals
            print("{} {} ${:.2f}".format(count+1, virtual_options[count],
                                         virtual_prices[count]))
        print("")
    # if user chose physical from order_type function prints physical menu
    else:
        print()
        # generates a series of numbers in the range of number_options
        for count in range(number_options):
            # formats menu for menu list to be ranged 1-8 options (not 0-8)
            # dollar sign added before menu
            # option prices and include price decimals
            print("{} {} ${:.2f}".format(count+1, physical_options[count],
                                         physical_prices[count]))
        print("")
    # continues program to menu_order function
    menu_order(p_v)


# nikoco commission menu
# takes p_v as a parameter
def menu_order(p_v):
    # identifies num_ordered and question with initial storage
    # MENU_LOW and MENU_HIGH as constants
    num_ordered = 0
    MENU_LOW = 1
    MENU_HIGH = 8
    question = ("")
    # ask if user wishes to create another order - prints instructions
    print("** Do you also wish to make a second commission? **")
    print("** Making another commission will prolong the time "
          "the order takes to be delivered to you. **")
    print("** If you do not, enter 1. If you do, enter 2: **")
# choose option of one or two orders - min 1, max 2 - using val_int function
    num_ordered = val_int(LOW, HIGH, question)
# choose options from menu (whether 1 or 2)
    print ("** Enter your", num_ordered, "commission(s) by "
           "entering its following number from the menu: **")
    # depending on the number of commissions chosen
    # item will count down a series of a string until finished
    for item in range(num_ordered):
        # if the num_ordered is greater than 0 user may
        # input a number from the menu until the number
        # of commissions they want is finished
        if num_ordered > 0:
            # count down until all pizzas are ordered
            commissions_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            # number inputted by user is equal
            # to the printed menu option number
            commissions_ordered = commissions_ordered - 1
        # if user chose virtual from order_type
        # function prints chosen menu option(s)
        # from the physical copy menu
        if p_v == "virtual":
            # prints chosen menu option(s) with name and price
            order_list.append(virtual_options[commissions_ordered])
            order_cost.append(virtual_prices[commissions_ordered])
            print("{} ${:.2f}" .format(virtual_options[commissions_ordered],
                                       virtual_prices[commissions_ordered]))
        # if user chose physical from order_type
        # function prints chosen menu option(s)
        # from the physical copy menu
        else:
            # prints chosen menu option(s) with name and price
            order_list.append(physical_options[commissions_ordered])
            order_cost.append(physical_prices[commissions_ordered])
            print("{} ${:.2f}" .format(physical_options[commissions_ordered],
                                       physical_prices[commissions_ordered]))
        # number inputted by user is equal to the number of commissions chosen
        num_ordered = num_ordered - 1


# print order out - including if order is del or pickup and
# names and price of each pizza - total cost including any delivery charge
# takes p_v as a parameter
def print_order(p_v):
    # total cost of order is summarized by all chosen order costs by user
    total_cost = sum(order_cost)
    # prints customer details, order details and order cost details
    print()
    print("----------------------------------")
    print("* Your Details")
    # exclusive only if user chose physical from order_type function
    if p_v == "physical":
        # created into format
        print(f"Customer Name: {customer_details['name']} "
              f"\nCustomer Phone:{customer_details['phone']} "
              f"\nCustomer Address: {customer_details['house']} "
              f"{customer_details['street']} {customer_details['suburb']}, "
              f"{customer_details['region']} {customer_details['postcode']}")
        print("You are ordering a physical copy- "
              "\nadditional shipping fee of $7.00")
        # adds $7 to total cost due to shipping fee
        total_cost = total_cost + 7
    # exclusive only if user chose virtual from order_type function
    elif p_v == "virtual":
        # created into format
        print(f"Customer Name: {customer_details['name']} "
              f"\nCustomer Phone: {customer_details['phone']} "
              f"\nCustomer Email: {customer_details['email']}")
        print("You are ordering a virtual copy.")
    print()
    print("** Your Order Details")
    # initial count variable
    count = 0
    # generates string of the commissions ordered
    # - displaying commission option name(s) and its cost
    for item in order_list:
        # prints in format
        print("Ordered: {}, ${:.2f}".format(item, order_cost[count]))
        # count of commissions is equal to commission menu options
        count = count + 1
    # prints total cost
    print()
    print("*** Order Cost Details")
    print(f"Your total cost is ${total_cost:.2f}")
    print("----------------------------------")
    print()


# cancel or proceed with order function
# takes p_v as a parameter
def order_confirm():
    # initial question variable
    question = ("")
    # prints instructions
    print ("** Please confirm your order... **")
    print ("To confirm, please enter '1' ")
    print ("To cancel, please enter '2' ")
    # confirm variable using val_int function for checking input errors
    confirm = val_int(LOW, HIGH, question)
    # if confirm variable is equal to 1 prints confirmation message
    if confirm == 1:
        print ()
        print ("Order Confirmed.")
        print ("** Your order has been sent to the artist "
               "and is now under review! **")
        print ("** We will contact you as soon as possible "
               "once your order has been accepted. **")
        print ()
        # sends user to new_exit function
        new_exit()
    # if confirm variable is else (therefore 2) prints cancel message
    else:
        print ()
        print ("Order Cancelled.")
        print ("** Your order has been cancelled! **")
        print()
        # sends user to new_exit function
        new_exit()


# option for new order only if cancelled or exit
def new_exit():
    # initial question variable
    question = ("")
    # prints instructions
    print ("** Do you wish to start another order or exit? **")
    print ("** A reminder that making another order must be "
           "under the name of a different user, or else this "
           "order will be discarded. **")
    print ("** Unless you had previously cancelled your order, "
           "you may use the same details as before with your "
           "new order. **")
    print ()
    print ("To start another order, please enter '1' ")
    print ("To exit the program, please enter '2' ")
    # confirm variable using val_int function for checking input errors
    confirm = val_int(LOW, HIGH, question)
    # if confirm variable is equal to 1 prints new order message
    if confirm == 1:
        print ("Starting new order...")
        print ()
        print ("...")
        # removes all previously stored input
        # from following arrays and dictionary
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        # sends user back to main function
        main()
    # if confirm variable is else (therefore 2) sends user to exit function
    else:
        exit()


# main function
# executes following functions
def main():
    """
    Purpose: to run all functions.
    Parameters: none
    Returns: none
    """
    welcome()
    p_v = order_type()
    detail_confirm(p_v)
    menu(p_v)
    print_order(p_v)
    order_confirm()

main()
