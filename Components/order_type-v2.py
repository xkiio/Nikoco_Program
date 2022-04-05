# Bugs
# menu so that user can choose either pickup or delivery
# no function for invalid input which is other than 1 or 2

print ("Do you want your order to be of virtual or physical use?")
print ("For a virtual copy, enter '1' ")
print ("For a physical copy, enter '2' ")

while True:
    try:
        virtual = int(input("Please enter a number: "))
        if virtual >= 1 and virtual <=2:
            if virtual == 1:
                print ("Virtual")
                break

            elif virtual == 2:
                print ("Physical")
                break
        else:
            print ("The number must be either 1 or 2.")
    except ValueError:
        print ("That is not a valid number.")
        print ("Please enter either 1 or 2.")