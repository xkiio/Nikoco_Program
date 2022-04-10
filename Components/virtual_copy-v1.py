#Bug - accepts blank input

print("Please enter your details for a virtual delivery.")

# customer name
valid = False
while not valid:
    name = input("Please enter your name: ")
    if name != "":
        print (name)
        break
    else:
        print ("Sorry, this cannot be blank.")

# customer phone number
valid = False
while not valid:
    phone = input("Please enter your phone number: ")
    if phone != "":
        print (phone)
        break
    else:
        print ("Sorry, this cannot be blank.")

# customer email
valid = False
while not valid:
    email = input("Please enter your email: ")
    if email != "":
        print (email)
        break
    else:
        print ("Sorry, this cannot be blank.")