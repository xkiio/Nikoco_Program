print ("** Do you wish to start another order or exit? **")
print ("** Reminder that making another order must be under the name of a different user, or else this order will be discarded. **")
print ("To start another order, please enter '1' ")
print ("To exit the program, please enter '2' ")
while True:
    try:
        confirm = int(input("Please enter a number: "))
        if confirm >= 1 and confirm <=2:
            if confirm == 1:
                print ("New Order.") 
                break
            elif confirm == 2:
                print ("Exit.")
                break
        else: # if input is invalid that is not 1 or 2 prints error message and loops
            print ("The number must be either 1 or 2.")
    except ValueError: # if input is invalid that is a foreign character or space prints error message and loops
        print ("That is not a valid number.")
        print ("Please enter either 1 or 2.")