customer_details = {"name": "Nuno","phone": "1234567876","house": "66","street": "Eve St","suburb": "Howick","region": "Auckland","postcode": "2010"}

# list to store ordered commissions
order_list = ['Poster Style','Square Canvas/Album Cover']
# list to store ordered commission prices
order_cost = [130, 60]

#print("\nCustomer Name: {}\nCustomer Phone: {}\nCustomer House Number: {}\nCustomer Street Name: {}\nCustomer Suburb: {}\nCustomer Region: {}\nCustomer Postcode: {}".format(customer_details['name'],customer_details['phone'],customer_details['house'],customer_details['street'],customer_details['suburb'],customer_details['region'],customer_details['postcode']))


print(f"{customer_details['name']} - {customer_details['phone']}, {customer_details['house']} {customer_details['street']} {customer_details['suburb']}, {customer_details['region']} {customer_details['postcode']}")


count = 0
for item in order_list:
    print("Ordered: {}, Cost ${:.2f}".format(item, order_cost[count]))
    count = count  +1