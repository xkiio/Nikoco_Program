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
num_ordered = 0

print("** Do you wish to make a second commission? **")
print("** Making another commission will prolong the time the order takes to be delivered to you. **")
num_ordered = int(input("If you do not, enter 1. If you do, enter 2: "))

print(num_ordered)

#Choose options from menu
print ("Please enter the following commissions you want by entering its number from the menu- ")
for item in range(num_ordered):
    if num_ordered > 0  :
        commissions_ordered = int(input())
        order_list.append(virtual_options[commissions_ordered])
        order_cost.append(virtual_prices[commissions_ordered])
        num_ordered = num_ordered - 1          

print(order_list)
print(order_cost)

# i want to make it so that the user is only limited to two orders, so their only optional input would be either 1 or 2. learn summm

            





#Count down until all pizzas are ordered



#print order