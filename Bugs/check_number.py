
def check_int(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return str(num)
            else:
                print("Phone numbers are limited between 7 and 15 digits.")
        except ValueError:
            print("Please enter your phone number- hyphens and spaces are not necessary.")


PH_LOW = 7
PH_HIGH = 15
question = ("Phone number: ")

phone = check_int(question, PH_LOW, PH_HIGH)
print(phone)

