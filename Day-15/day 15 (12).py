print("12. map() FUNCTION")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)
names = ["teja", "ravi", "sneha"]
upper_names = list(map(lambda name: name.upper(), names))
print("Uppercase names:", upper_names)
prices = [1000, 2000, 3000]
with_gst = list(map(lambda x: x + (x * 0.18), prices))
print("Prices with GST:", with_gst)
words = ["python", "java", "sql"]
lengths = list(map(lambda word: len(word), words))
print("Word lengths:", lengths)
