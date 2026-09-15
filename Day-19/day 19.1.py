print("3. PRODUCT NAMES → UPPERCASE")
products = ["laptop", "phone", "tablet", "monitor"]
upper_products = [p.upper() for p in products]
print("Upper products:", upper_products)

print("4. APPLY 10% DISCOUNT ON PRICES")
prices = [1000, 800, 450, 300]
discounted = [price * 0.9 for price in prices]
print("Discounted prices:", discounted)

print("5. GET INDEXES OF PRODUCTS IN STOCK")
in_stock = [True, False, True, False]
available = [i for i, stock in enumerate(in_stock) if stock]
print("Available indexes:", available)

print("6. FILTER PRODUCTS WITH PRICE > 700 (Tuples)")
product_info = [("Laptop", 1000), ("Phone", 800), ("Tablet", 450)]
expensive = [name for name, price in product_info if price > 700]
print("Expensive products:", expensive)


