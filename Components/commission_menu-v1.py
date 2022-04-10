# virtual commissions
virtual_options = ['Landscape Layout','Portrait (Full body)','Portrait (Half body)','Square Canvas/Album Cover','Wallpaper- Laptop/Tablet','Wallpaper- Iphone','Character Design Ref','Profile Picture',]

virtual_prices = [150, 100, 80, 60, 50, 50, 30, 10]

def menu_virtual():
    number_options = 8
    for count in range(number_options) :
        print("{} {} ${:.2f}" .format(count+1, virtual_options[count],virtual_prices[count]))

menu_virtual()


# physical commissions
physical_options = ['Landscape Layout','Poster Style','Portrait (Full body)','Portrait (Half body)','Square Canvas/Album Cover','Character Design Collage','Iphone Case','Sticker Designs (x5)',]

physical_prices = [150, 130, 100, 80, 60, 35, 15, 10]

def menu_physical():
    number_options = 8
    for count in range(number_options) :
        print("{} {} ${:.2f}" .format(count+1, physical_options[count],physical_prices[count]))

menu_physical()