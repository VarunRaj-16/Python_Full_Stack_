print("9. NESTED LIST COMPREHENSION (Flatten Colors)")
products_colors = [
    {"name": "Laptop", "colors": ["Silver", "Black"]},
    {"name": "Phone", "colors": ["Gold", "Blue"]}
]
all_colors = [color for product in products_colors for color in product["colors"]]
print("All colors:", all_colors)

print("10. AVAILABLE PRODUCTS WITH DISCOUNTED PRICE")
products_data = [
    {"name": "Laptop", "price": 1000, "stock": 3},
    {"name": "Phone", "price": 800, "stock": 0},
    {"name": "Tablet", "price": 450, "stock": 5}
]
result = [f"{p['name']} - ${p['price'] * 0.9:.2f}" for p in products_data if p["stock"] > 0]
print(result)
