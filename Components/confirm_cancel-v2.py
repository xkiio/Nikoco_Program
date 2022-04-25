def order_confirm():
    print ("** Please confirm your order... **")
    print ("To confirm, please enter '1' ")
    print ("To cancel, please enter '2' ")
    while True:
        try:
            confirm = int(input("Please enter a number: "))
            if confirm >= 1 and confirm <=2:
                if confirm == 1:
                    print ("Order Confirmed.")
                    print ("** Your order has been sent to the artist and is now under review! **")
                    print ("** We will contact you as soon as possible when your order has been accepted. **")
                    print ("** Once we have recieved the required information about your order, we shall begin the process ^^ **")
                    break
                elif confirm == 2:
                    print ("Order Cancelled.")
                    print ("** Your order has been cancelled! **")
                    print ("** You can restart your order or exit the program. **")
                    break
            else: # if input is invalid that is not 1 or 2 prints error message and loops
                print ("The number must be either 1 or 2.")
        except ValueError: # if input is invalid that is a foreign character or space prints error message and loops
            print ("That is not a valid number.")
            print ("Please enter either 1 or 2.")

order_confirm()