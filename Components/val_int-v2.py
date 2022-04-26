def order_type(low, high, question):
    while True: # sets up while loop
        try: # allows two options that is either 1 or 2
            num = int(input(question))
            if num >= low and num <= high: # if input is equal to 1 or 2 
                return num
            else: # if input is invalid prints error message
                print ("Please enter a number that is either", low, "or" , high)
        except ValueError: # if input is exceptional to invalid number and is instead an invalid character
            print ("That is not a valid number.") # prints error message
            print ("Please enter a number that is either", low, "or" , high)

LOW = 1
HIGH = 2
question = (f"Order type: ")
answer = order_type(LOW, HIGH, question)

print(answer)