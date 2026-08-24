#Functions

def greet(name):
    return f"Hello, {name}! Welcome to the world of programming."


print("\nFunction with parameter:")
name = "Nazmun Sakib"
greeting_message = greet(name)
print(greeting_message)

#Function with default parameter
def greet_with_default(name="Guest"):
    return f"Hello, {name}! Welcome to the world of programming."

print("\nFunction with default parameter:")
greeting_message_default = greet_with_default()
print(greeting_message_default);

#Function with multiple parameters
def add_numbers(a, b):
    return a + b

print("\nFunction with multiple parameters:")
num1 = 10
num2 = 20
sum_result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")

def get_price_category(price):
    if price > 200:
        return "Very Expensive"
    elif price > 100:
        return "Expensive"
    elif price > 50:
        return "Moderate"
    else:
        return "Affordable"

print("\nFunction with conditional logic:")
products = [
    {"name": "Laptop", "price": 1500},
    {"name": "Book", "price": 20},
    {"name": "Headphones", "price": 100}
]

for product in products:
    category = get_price_category(product["price"])
    print(f"Product: {product['name']} | Price: {product['price']} | Category: {category}")

def is_even(number):
    return number % 2 == 0

print("\nFunction with conditional logic:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numbers:
    if is_even(n):
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")

#function with type hints
def multiply_numbers(a: int, b: int) -> int:
    return a * b

print("\nFunction with type hints:")
result = multiply_numbers(5, 3)
print(f"The product of 5 and 3 is: {result}")