customer_details = {"name": "Nuno","phone": "1234567876","house": "66","street": "Eve St","suburb": "Howick","region": "Auckland","postcode": "2010"}

# list to store ordered commissions
order_list = ['Poster Style','Square Canvas/Album Cover']
# list to store ordered commission prices
order_cost = [130, 60]

def print_order():
    total_cost = sum(order_cost)
    print()
    print("----------------------------------")
    print("* Customer Details")
    print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}, {customer_details['region']} {customer_details['postcode']}")
    print()
    print("** Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}, ${:.2f}".format(item, order_cost[count]))
        count = count  +1
    print()
    print("*** Order Cost Details")
    print(f"Your total cost is ${total_cost:.2f}")
    print("----------------------------------")
    print()

print_order()