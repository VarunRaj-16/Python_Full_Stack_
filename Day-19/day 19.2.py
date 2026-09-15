print("7. LIST OF DICTIONARIES")
products_data = [
    {"name": "Laptop", "price": 1000, "stock": 3},
    {"name": "Phone", "price": 800, "stock": 0},
    {"name": "Tablet", "price": 450, "stock": 5}
]
available_names = [p["name"] for p in products_data if p["stock"] > 0]
print("Available product names:", available_names)
discounted_products = [{p["name"]: p["price"] * 0.9} for p in products_data if p["stock"] > 0]
print("Discounted products:", discounted_products)

print("8. LIST COMPREHENSION WITH DIFFERENT DATA TYPES")
fruits = ["apple", "banana", "mango"]
print("Uppercase strings:", [s.upper() for s in fruits])
prices = [1200, 800, 450]
print("Add 100 to prices:", [x + 100 for x in prices])
float_prices = [99.99, 49.50, 199.99]
print("Increase by 10% and round:", [round(p * 1.1, 2) for p in float_prices])


