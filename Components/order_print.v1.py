
customer_details = {"name": "nuno","phone": "1234567876","house": "66","street": "Eve St","suburb": "Howick","region": "Auckland","postcode": "2010"}

# list to store ordered commissions
order_list = ['Poster Style','Square Canvas/Album Cover']
# list to store ordered commission prices
order_cost = [130, 60]

count = 0
for item in order_cost:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count  +1
