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

# constants
LOW = 1
HIGH = 2    

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


# validates inputs to check if they are blank.
# takes question as a parameter
# returns response in title class if valid
# - capitalizes first letter of words' input
def not_blank(question):
    valid = False
    while not valid:
        # sets up while loop
        response = input(question)
        # asks for input(string)
        if response != "":
            # if input is valid prints response and continues other functions.
            return response.title()
        else:
            # if input is invalid prints error message
            print("This cannot be blank.")

def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters.")
        else:
            return response.title()


# validates inputs to check if they are an integer.
def val_int(low, high, question):
    while True:
        # sets up while loop
        try:
            # allows two options that is either 1 or 2
            num = int(input(question))
            if num >= low and num <= high:
                # if input is equal to 1 or 2
                return num
            else:
                # if input is invalid prints error message
                print ("Please enter a number that is either", low, "or", high)
        except ValueError:
            # if input is exceptional to invalid
            # number and is instead an invalid character
            print ("That is not a valid number.")
            # prints error message
            print ("Please enter a number that is either", low, "or", high)


def exit():
        print ()
        print ("** Thank you for using our Nikoco Commissions"
               "Program! We hope to see you again! **")
        print ()
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()


# defining welcome page
def welcome():
    """
    Purpose: to generate a random name for the list and and print out
    a welcome message.
    Parameters: none
    Returns: none
    """
    num = randint(0, 7)
    # randomized number from 0 to 7
    name = (names[num])
    # assigns each given name with a number from 0 to 7
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
    y_or_n()


# yes or no condition funtion input
def y_or_n():
    while True:
        try:
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


# n function if user inputs n for conditions
def n():
    question = ("")
    print("")
    print("** I'm sorry, you must agree to these terms "
          "in order to commission the artist. **")
    print("** If you wish to restart the program, type 1 **")
    print("** If you wish to exit the program, type 2 **")
    restart = val_int(LOW, HIGH, question)
    # asks for input
    if restart == 1:
        # if input is 1 sends user to reboot
        print ()
        print ("Restarting program...")
        main()
    else:
        # if input is 2 aborts program and prints farewell message
        exit()


# order_type function and printing instructions
def order_type():
    p_v = ""
    question = ("")
    print("")
    print ("** Do you want your order to be of virtual or physical use? **")
    print ("** For a virtual copy, enter '1' **")
    print ("** For a physical copy, enter '2' **")
    virtual = val_int(LOW, HIGH, question)
    # asks for input
    if virtual == 1:
        # if input is 1 follows virtual order function
        print ("")
        print ("** For a virtual delivery, we would like your name, "
               "phone number, and email address where the final "
               "product will be sent! **")
        print ("** It is important that your details are correct- "
               "if you have made a mistake, you can reset your "
               "details after full input. **")
        p_v = "virtual"
        virtual_info()
    else:
        # if input is 2 foll ows physical order function (NOT virtual function)
        print ("")
        print ("** For a physical delivery, we would like your "
               "name, phone number "
               "and home address where the final product will be sent! **")
        print ("** It is important that your details are correct- if you have"
               " made a mistake, you can redo your details after "
               "a full input. **")
        p_v = "physical"
        physical_info()
    return p_v
    # returns parameter's result back whether physical or virtual


# virtual_info function - name, phone number and email address
def virtual_info():
    # basic instructions
    print ("** Please enter the following... **")
    question = ("Name: ")
    # asks for name
    customer_details['name'] = check_string(question)
    # print(customer_details['name'])

    question = ("Phone number: ")
    # asks for phone number
    customer_details['phone'] = not_blank(question)
    # print(customer_details['phone'])

    question = ("Email address: ")
    # asks for email address
    customer_details['email'] = not_blank(question)
    # print(customer_details['email'])
    print()


# physical_info function - house address and phone
def physical_info():
    # basic instructions
    print ("** Please enter the following... **")
    question = ("Name: ")
    # asks for name
    customer_details['name'] = check_string(question)
    # print(customer_details['name'])

    question = ("Phone number: ")
    # asks for phone number
    customer_details['phone'] = not_blank(question)
    # print(customer_details['phone'])

    question = ("House number: ")
    # asks for house number
    customer_details['house'] = not_blank(question)
    # print(customer_details['house'])

    question = ("Street name: ")
    # asks for street name
    customer_details['street'] = check_string(question)
    # print(customer_details['street'])

    question = ("Suburb: ")
    # asks for suburb name
    customer_details['suburb'] = check_string(question)
    # print(customer_details['suburb'])

    question = ("State/city: ")
    # asks for state/city name
    customer_details['region'] = check_string(question)
    # print(customer_details['region'])

    question = ("Postcode: ")
    # asks for postcode
    customer_details['postcode'] = not_blank(question)
    # print(customer_details['postcode'])
    print()


def detail_confirm(p_v):
    question = ("")
    print ("** Please confirm your details... **")
    print ("To confirm, please enter '1' ")
    print ("To try again, please enter '2' ")
    detail = val_int(LOW, HIGH, question)
    if detail == 1:
        print ("Details Confirmed.")
    else:
        print ("Details Cancelled.")
        print ()
        if p_v == "virtual":
            virtual_info()
            customer_details.clear
            detail_confirm(p_v)
        else:
            physical_info()
            customer_details.clear
            detail_confirm(p_v)


def menu(p_v):
    number_options = 8
    if p_v == "virtual":
        print()
        for count in range(number_options):
            print("{} {} ${:.2f}".format(count+1, virtual_options[count],
                                         virtual_prices[count]))
        print("")
    else:
        print()
        for count in range(number_options):
            print("{} {} ${:.2f}".format(count+1, physical_options[count],
                                         physical_prices[count]))
        print("")
    menu_order(p_v)


# nikoco commission menu - virtual
def menu_order(p_v):
    num_ordered = 0
    MENU_LOW = 1
    MENU_HIGH = 8
    question = ("")
    # ask if user wishes to create another order.
    print("** Do you also wish to make a second commission? **")
    print("** Making another commission will prolong the time "
          "the order takes to be delivered to you. **")
    print("** If you do not, enter 1. If you do, enter 2: **")
# choose option of one or two orders - min 1, max 2
    num_ordered = val_int(LOW, HIGH, question)
# choose options from menu
    print ("** Enter your", num_ordered, "commission(s) by "
           "entering its following number from the menu: **")
    for item in range(num_ordered):
        if num_ordered > 0:
            commissions_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            commissions_ordered = commissions_ordered - 1
            # Count down until all pizzas are ordered
        if p_v == "virtual":
            order_list.append(virtual_options[commissions_ordered])
            order_cost.append(virtual_prices[commissions_ordered])
            print("{} ${:.2f}" .format(virtual_options[commissions_ordered],
                                       virtual_prices[commissions_ordered]))
            # count down until all pizzas are ordered
        else:
            order_list.append(physical_options[commissions_ordered])
            order_cost.append(physical_prices[commissions_ordered])
            print("{} ${:.2f}" .format(physical_options[commissions_ordered],
                                       physical_prices[commissions_ordered]))
        num_ordered = num_ordered - 1


# print order out - including if order is del or pickup and
# names and price of each pizza - total cost including any delivery charge
def print_order(p_v):
    total_cost = sum(order_cost)
    print()
    print("----------------------------------")
    print("* Your Details")
    if p_v == "physical":
        print(f"Customer Name: {customer_details['name']} "
              f"\nCustomer Phone:{customer_details['phone']} "
              f"\nCustomer Address: {customer_details['house']} "
              f"{customer_details['street']} {customer_details['suburb']}, "
              f"{customer_details['region']} {customer_details['postcode']}")
        print("You are ordering a physical copy- "
              "\nadditional shipping fee of $7.00")
        total_cost = total_cost + 7
    elif p_v == "virtual":
        print(f"Customer Name: {customer_details['name']} "
              f"\nCustomer Phone: {customer_details['phone']} "
              f"\nCustomer Email: {customer_details['email']}")
        print("You are ordering a virtual copy.")
    print()
    print("** Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}, ${:.2f}".format(item, order_cost[count]))
        count = count + 1
    print()
    print("*** Order Cost Details")
    print(f"Your total cost is ${total_cost:.2f}")
    print("----------------------------------")
    print()


# cancel or proceed with order
def order_confirm(p_v):
    question = ("")
    print ("** Please confirm your order... **")
    print ("To confirm, please enter '1' ")
    print ("To cancel, please enter '2' ")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ()
        print ("Order Confirmed.")
        print ("** Your order has been sent to the artist "
               "and is now under review! **")
        print ("** We will contact you as soon as possible "
               "once your order has been accepted. **")
        print ()
        new_exit()
    else:
        print ()
        print ("Order Cancelled.")
        print ("** Your order has been cancelled! **")
        print()
        new_exit()


# option for new order only if cancelled or exit
def new_exit():
    question = ("")
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
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("Starting new order...")
        print ()
        print ("...")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()
    else:
        exit()


# main function
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
    order_confirm(p_v)

main()
