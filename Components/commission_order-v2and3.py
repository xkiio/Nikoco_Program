# virtual commissions
virtual_options = ['Landscape Layout','Portrait (Full body)','Portrait (Half body)','Square Canvas/Album Cover','Wallpaper- Laptop/Tablet','Wallpaper- Iphone','Character Design Ref','Profile Picture',]
# list of virtual prices
virtual_prices = [150, 100, 80, 60, 50, 50, 30, 10]

#list to store ordered options
order_list = []
#list to store option's prices
order_cost = []

#list to store order cost
def menu_virtual():
    number_ordered = 8

    for count in range(number_ordered) :
        print("{} {} ${:.2f}" .format(count+1, virtual_options[count],virtual_prices[count]))

menu_virtual()
print("")

# ask if user wishes to create another order.
print("** Do you wish to make a second commission? **")
print("** Making another commission will prolong the time the order takes to be delivered to you. **")
print("** If you do not, enter 1. If you do, enter 2: **")
num_ordered = 0
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
print ("** Enter the following commission you want by entering its following number from the menu: **")
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
        commissions_ordered = commissions_ordered -1
        order_list.append(virtual_options[commissions_ordered])
        order_cost.append(virtual_prices[commissions_ordered])
        print("{} ${:.2f}" .format(virtual_options[commissions_ordered],virtual_prices[commissions_ordered]))
        num_ordered = num_ordered - 1          

print(order_list)
print(order_cost)
            





#Count down until all pizzas are ordered



#print order