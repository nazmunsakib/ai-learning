#IF

price = 40
products = ["Laptop", "Smartphone", "Headphones", "Monitor"]
product_prices = {"Laptop": 1000, "Smartphone": 500, "Headphones": 100, "Monitor": 300}

#elif
if price > 200:
    print("Very Expensive")
elif price > 100:
    print("Expensive")
elif price > 50:
    print("Moderate")
else:
    print("Affordable")

#Conditional Statements with Lists
if "Laptop" in products:
    print("Laptop is available in the product list.")

#conditional statements with dictionaries
if "Laptop" in product_prices:
    print("Laptop is available in the product prices dictionary.")
    