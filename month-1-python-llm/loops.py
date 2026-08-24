products = ["Laptop", "Smartphone", "Headphones", "Monitor"]
product_set = [
    {"Name": "Laptop", "Price": 1000},
    {"Name": "Smartphone", "Price": 500},
    {"Name": "Headphones", "Price": 100},
    {"Name": "Monitor", "Price": 300}
]

#Looping through the list of products
print("Looping through the list of products:")
for product in products:
    print("Product:", product)

#Looping through the dictionary of product prices
product_prices = {"Laptop": 1000, "Smartphone": 500, "Headphones": 100, "Monitor": 300}
print("\nLooping through the dictionary of product prices:")
for product, price in product_prices.items():
    print("Product:", product, "| Price:", price)

#Looping through the list of products with index
print("\nLooping through the list of products with index:")
for index, product in enumerate(products):
    print("Index:", index, "| Product:", product)

#range function to loop through a range of numbers
print("\nLooping through a range of numbers from 0 to 4:")
for i in range(1, 6):
    print("Number:", i)

#Looping with condition
print("\nLooping with condition:")
for product in product_set:

    if product["Price"] >= 500:
        print("Product:", product["Name"], "| Price:", product["Price"], "| Status: Expensive")
    else:
        print("Product:", product["Name"], "| Price:", product["Price"], "| Status: Affordable")