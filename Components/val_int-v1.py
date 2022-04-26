def order_type():
    while True: # sets up while loop
        try: # allows two options that is either 1 or 2
            num = int(input())
            if num >= 1 and num <=2: # if input is equal to 1 or 2 
                return num

            else: # if input is invalid prints error message
                print ("The number must be either 1 or 2.")
        except ValueError: # if input is exceptional to invalid number and is instead an invalid character
            print ("That is not a valid number.") # prints error message
            print ("Please enter either 1 or 2.")

print ("Enter a number that is either 1 or 2. ")
answer = order_type()

print(answer)